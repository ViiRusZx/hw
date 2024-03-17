from weather import get_weather
from fastapi import FastAPI

app = FastAPI()


@app.get("/weather")
def testing():
    weather = get_weather("Moscow,Russia")
    if weather:
        return f"Погода в Москве: {weather['temp_C']}, Ощущается как: {weather['FeelsLikeC']}"
    else:
        return "Не удалось определить погоду"
