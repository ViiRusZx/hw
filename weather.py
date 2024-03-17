import requests

weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"


def get_weather(city):
    parametrs = {"key": "47c353c880f74379ae783035241703", "q": city, "format": "json",
                 "num_of_days": 1, "lang": "ru"}
    res = requests.get(weather_url, parametrs)
    weather = res.json()
    if "data" in weather:
        if "current_condition" in weather["data"]:
            try:
                return weather["data"]["current_condition"][0]
            except TypeError:
                return False
    return weather
