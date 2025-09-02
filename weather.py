import requests

API_KEY = "ef0c1aa981153357d0f7afd828488ded".strip()
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if not city:
        return "⚠️ Please enter a city name."

    print(f"DEBUG: Requesting weather for {city} with API_KEY={API_KEY[:5]}...")  # only show first 5 chars
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        condition = data["weather"][0]["description"].capitalize()
        return f"🌍 Weather in {city.title()}:\n🌡️ Temp: {temp}°C (feels like {feels_like}°C)\n☁️ Condition: {condition}"
    else:
        return f"❌ Error {response.status_code}: {response.json().get('message','Unknown error')}"
