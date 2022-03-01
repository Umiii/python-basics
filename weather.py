import requests
import json

API_KEY = "1c1fce396d8bf6b56edc13a4a4ba27c6"
city="Orlando"
url = "http://api.openweathermap.org/data/2.5/find?q="+city+"&appid="+API_KEY+"&units=imperial"

request = requests.get(url)
json_response = request.json()

description = json_response["list"][0].get("weather")[0].get("description")
print("Today's forecast is", description)
temp_min = json_response.get("list")[0].get("main").get("temp_min")
print("The minimum temperature is", temp_min)
temp_max = json_response.get("list")[0].get("main").get("temp_max")
print("The maximum temperature is", temp_max)