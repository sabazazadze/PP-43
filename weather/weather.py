# სავარჯიშო 3: მოცემული კოდი (არ შეცვალოთ)
import requests

URL = "https://api.weather-demo.ge/current"


def get_temperature(city):
    response = requests.get(URL, params={"city": city}, timeout=5)
    return response.json()["temp"]


def weather_message(city):
    temp = get_temperature(city)
    if temp >= 25:
        return f"{city}: {temp}°C, ცხელა"
    if temp <= 0:
        return f"{city}: {temp}°C, ყინავს"
    return f"{city}: {temp}°C, კარგი ამინდია"