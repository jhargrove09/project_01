import requests

url = 'http://api.weatherapi.com/v1/current.json?key=93bf06f9f0974f6b81840149260503&q=Orlando&aqi=no'
response = requests.get(url)
weather_json = response.json()

print(weather_json)