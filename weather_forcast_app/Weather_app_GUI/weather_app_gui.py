import tkinter as tk
from tkinter import messagebox
from api_helper import get_weather_data
from gui_helpers import extract_weather_info, display_weather_info
from config import API_KEY

def get_weather_info():
    city_or_zip = entry.get()
    weather_data = get_weather_data(city_or_zip, API_KEY)

    if weather_data["cod"] == 200:
        temperature, humidity, wind_speed, description = extract_weather_info(weather_data)
        display_weather_info(result_text, city_or_zip, temperature, humidity, wind_speed, description)
    else:
        messagebox.showerror("Error", "Unable to retrieve weather data. Please check your input.")

# Create the main window
root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("400x300")

# Create components
label = tk.Label(root, text="Enter the name of a city or a zip code:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Get Weather", command=get_weather_info)
button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
