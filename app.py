import uvicorn
import pickle
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

import warnings
warnings.filterwarnings('ignore')

from model_utils import get_tfidf_features, predict_bug

# Load model inference related files
loaded_vec = pickle.load(open("model_files/feature_vectorizer.pkl", "rb"))
selector = pickle.load(open("model_files/selector.pkl", "rb"))
model = pickle.load(open('model_files/mlp.pkl', 'rb'))

app = FastAPI()

# Allow anyone to call the API from their own apps
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/classify", response_class=HTMLResponse)
async def classify(request: Request):
    return templates.TemplateResponse("classify.html", {"request": request})

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    title, description = data['title'], data['description']
    features = get_tfidf_features(title, description, loaded_vec, selector)
    prediction = predict_bug(features, model)
    return {"prediction": prediction}

if __name__ == '__main__':
    uvicorn.run("app:app", reload=True)