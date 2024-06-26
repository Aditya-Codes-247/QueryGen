from fastapi import APIRouter, UploadFile, File, HTTPException
from PIL import Image
import io
import pytesseract
from services.sql_service import generate_sql_ddl
from services.image_service import extract_table_structure_from_image
from services.sql_service import generate_sql
router = APIRouter()

@router.post("/generate_sql_from_image/")
def create_sql_command_from_image(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(file.file.read()))
        prompt = pytesseract.image_to_string(image)
        sql_command = generate_sql(prompt)
        return {"sql_command\n": sql_command}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate_ddl_sql_from_image/")
async def create_ddl_sql_command_from_image(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read()))
        table_structure = extract_table_structure_from_image(image)
        if not table_structure:
            raise HTTPException(status_code=400, detail="Could not extract table structure from image")
        prompt = f"Create a table named <table_name> with the columns: {table_structure}"
        sql_command_ddl = generate_sql_ddl(prompt)
        return {"sql_command\n": sql_command_ddl}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
