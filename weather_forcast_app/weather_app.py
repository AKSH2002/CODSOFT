from api_helper import get_weather_data
from config import API_KEY

def get_user_input():
    user_input = input("Enter the name of a city or a zip code: ")
    return user_input

def extract_weather_info(data):
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]
    return temperature, humidity, wind_speed, description

def display_weather_info(city, temperature, humidity, wind_speed, description):
    print(f"Weather information for {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Description: {description.capitalize()}")

def main():
    city_or_zip = get_user_input()
    weather_data = get_weather_data(city_or_zip, API_KEY)

    if weather_data["cod"] == 200:
        temperature, humidity, wind_speed, description = extract_weather_info(weather_data)
        display_weather_info(city_or_zip, temperature, humidity, wind_speed, description)
    else:
        print("Error: Unable to retrieve weather data. Please check your input.")

if __name__ == "__main__":
    main()
