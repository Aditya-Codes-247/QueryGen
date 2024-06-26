from fastapi import APIRouter, UploadFile, File, HTTPException
from pydub import AudioSegment
from io import BytesIO
import speech_recognition as sr
from services.sql_service import generate_sql
router = APIRouter()


@router.post("/generate_sql_from_voice/")
async def create_sql_command_from_voice(file: UploadFile = File(...)):
    try:
        # Ensure the uploaded file is in PCM format (required for WAV)
        audio = AudioSegment.from_file(BytesIO(await file.read()))

        # Convert to PCM WAV format if not already in that format
        if audio.frame_rate != 16000 or audio.sample_width != 2:
            audio = audio.set_frame_rate(16000).set_sample_width(2)

        # Write the converted audio to a BytesIO object
        wav_file = BytesIO()
        audio.export(wav_file, format="wav")

        # Reset the file pointer of BytesIO object to the beginning
        wav_file.seek(0)

        # Process the WAV file with speech recognition
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_file) as source:
            audio = recognizer.record(source)
        prompt = recognizer.recognize_google(audio)

        # Perform SQL generation based on recognized prompt
        sql_command = generate_sql(prompt)  # You need to implement this function

        return {"sql_command\n": sql_command}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
