from fastapi import FastAPI
from scraper import get_weather

app = FastAPI()

@app.get("/weather/{city}")
def weather(city: str):
    return get_weather(city)
