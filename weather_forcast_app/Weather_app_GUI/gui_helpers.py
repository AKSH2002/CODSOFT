def extract_weather_info(data):
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]
    return temperature, humidity, wind_speed, description

def display_weather_info(result_text, city, temperature, humidity, wind_speed, description):
    result_text.set(f"Weather information for {city}:\n"
                    f"Temperature: {temperature}°C\n"
                    f"Humidity: {humidity}%\n"
                    f"Wind Speed: {wind_speed} m/s\n"
                    f"Description: {description.capitalize()}")
