import os
import sys
import requests
from dotenv import load_dotenv

# Load variables from .env file into environment variables
load_dotenv()

# get the api key from the environment
key=os.getenv("weather_api_key")
if not key:
        print("Error: API key not found. Please set the 'weather_api_key' environment variable.")
        sys.exit() 


name =input("please enter the name of the city you want to get the weather report for:")


#url for the geocoding api 
url = f"http://api.openweathermap.org/geo/1.0/direct?q={name}&limit=1&appid={key}"


response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    if not data:
        print("City not found.")
        sys.exit()
elif response.status_code == 401:
    print("Unauthorized: Invalid API key.")
    sys.exit()
else:
    print(f"Error fetching data: {response.status_code}")
    sys.exit()

result = data[0]
lat = result['lat']    
lon = result['lon']
city_name = result["name"]

url= f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"] - 273.15
    feels_like = data["main"]["feels_like"] - 273.15
    print(f"Today's weather on {city_name} is gonna be {data['weather'][0]['description']} with a temperature of {temp:.2f}°C, but it's gonna feel like {feels_like:.2f}°C.")
else:
    print(f"Error fetching weather: {response.status_code}")
