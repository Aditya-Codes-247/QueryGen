from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()

# Set up the templates directory
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/ddl", response_class=HTMLResponse)
async def read_ddl(request: Request):
    return templates.TemplateResponse("ddl.html", {"request": request})

@router.get("/dml", response_class=HTMLResponse)
async def read_dml(request: Request):
    return templates.TemplateResponse("dml.html", {"request": request})
