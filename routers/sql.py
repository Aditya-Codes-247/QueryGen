from fastapi import APIRouter, HTTPException
from models.schemas import TextPrompt
from services.sql_service import generate_sql, generate_sql_ddl

router = APIRouter()

@router.post("/generate_sql/")
def create_sql_command(text_prompt: TextPrompt):
    try:
        sql_command = generate_sql(text_prompt.prompt)
        return {"sql_command\n": sql_command}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate_ddl_sql/")
def create_ddl_sql_command(text_prompt: TextPrompt):
    try:
        sql_command_ddl = generate_sql_ddl(text_prompt.prompt)
        return {"sql_command\n": sql_command_ddl}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
