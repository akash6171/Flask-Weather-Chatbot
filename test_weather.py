import requests

API_KEY = "ef0c1aa981153357d0f7afd828488ded"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = "London"
params = {"q": city, "appid": API_KEY, "units": "metric"}
response = requests.get(BASE_URL, params=params)
print(response.json())
