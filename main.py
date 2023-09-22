from fastapi import FastAPI, Request, Form
from functions import number_to_words, luck_game
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

# Mount the "static" directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    return "hello world"


@app.get("/form")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post("/form")
def form_post(request: Request, num: int = Form(...)):
    result = number_to_words(num)
    return templates.TemplateResponse('form.html', context={"request": request, 'result': result})


@app.get("/luck")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('form2.html', context={'request': request, 'result': result})


@app.post("/luck")
def form_post(request: Request, num: int = Form(...)):
    result = luck_game(num)
    return templates.TemplateResponse('form2.html', context={"request": request, 'result': result})


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
