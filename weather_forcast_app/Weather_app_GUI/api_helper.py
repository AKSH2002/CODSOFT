import requests

def get_weather_data(user_input, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": user_input,
        "appid": api_key,
        "units": "metric"  # For Celsius temperature. Use "imperial" for Fahrenheit.
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    return data
