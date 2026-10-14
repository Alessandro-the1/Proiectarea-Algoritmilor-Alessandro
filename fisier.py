from dotenv import load_dotenv
import os
import requests
 
load_dotenv()
 
cheie_api_openweather = os.getenv("API_KEY")

url_geocoding = "https://api.openweathermap.org/geo/1.0/direct?"
oras = input("Introdu numele orasului: ")
raspuns_geocoding = requests.get(url_geocoding, params={
    'q':oras,
    "appid": cheie_api_openweather
}).json()

url = "https://api.openweathermap.org/data/2.5/weather?"
lat = raspuns_geocoding[0]['lat']
lon = raspuns_geocoding[0]['lon']
raspuns = requests.get(url, params={
    "lat": lat,
    "lon": lon,
    "units": "metric",
    "lang":'ro',
    "appid":cheie_api_openweather
}).json()

starea_vremii = raspuns['weather'][0]['description']
temperatura = raspuns['main']['temp']
viteza_vant = raspuns['wind']['speed']

print(f"In {oras} sunt {temperatura} grade, vantul bate cu {viteza_vant} km/h, iar starea vremii este {starea_vremii}")