import requests
from pprint import pprint

API = 'abb83b4e43fae2414a7534cc16e5d683'

City= input("Enter your city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API +"&q="+City

weather_data = requests.get(base_url).json()

pprint(weather_data)