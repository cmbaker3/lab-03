import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "41ba3c7d4b9457b0103f7307fcbd4113"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)
URL2 = "https://official-joke-api.appspot.com/random_joke"

def random_joke() -> Dict:
    res2 = requests.get(URL2, params={})
    return res2.json()

def main():
    temp = get_weather("London")
    print(temp)

if __name__ == "__main__":
    main()
