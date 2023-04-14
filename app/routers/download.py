from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates/")



@router.get("/download", response_class=HTMLResponse)
def get_accordion(request: Request):
    tag = "flower"
    result = "Type a number"
    return templates.TemplateResponse('download.html', context={'request': request, 'result': result, 'tag': tag})


@router.post("/download", response_class=HTMLResponse)
def post_accordion(request: Request, tag: str = Form(...)):

    return templates.TemplateResponse('download.html', context={'request': request, 'tag': tag})

    