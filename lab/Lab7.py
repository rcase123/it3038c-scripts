import requests

from pprint import pprint

#importing the plug ins

API = 'abb83b4e43fae2414a7534cc16e5d683'

#This is my personal API from openweather.com.

City = raw_input("Enter your city: ")

#This is the input for the city to search for the weather.
#The website has limitations in searching, but you can be more specific by adding ,US after.
#Either one works.

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API + "&q=" + City

#This is piecing together the input with a url, api and the input.

weather_data = requests.get(base_url).json()

#This uses the request plug in and the baseurl variable to pull the information from the site.

pprint(weather_data)

#This prints all data involved
