import requests
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
import time

class WeatherApp:
    def __init__(self):
        self.base_url = "https://api.open-meteo.com/v1/forecast"
        self.geocoder = Nominatim(user_agent="weather_app")
    
    def get_city_coordinates(self, city_name):
        """
        Get latitude and longitude for a given city name.
        Returns the closest matching city coordinates.
        """
        try:
            location = self.geocoder.geocode(city_name, timeout=10)
            if location:
                return location.latitude, location.longitude, location.address
            else:
                print(f"City '{city_name}' not found. Please try again.")
                return None, None, None
        except Exception as e:
            print(f"Error geocoding city: {e}")
            return None, None, None
    
    def get_weather_forecast(self, latitude, longitude, city_name):
        """
        Fetch weather forecast data from Open-Meteo API.
        Returns weather info for today and tomorrow.
        """
        try:
            params = {
                "latitude": latitude,
                "longitude": longitude,
                "daily": "weather_code,temperature_2m_max,temperature_2m_min,wind_speed_10m_max",
                "timezone": "auto"
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
    
    def interpret_weather_code(self, code):
        """
        Convert WMO weather code to human-readable description.
        """
        weather_descriptions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Foggy",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snow",
            73: "Moderate snow",
            75: "Heavy snow",
            77: "Snow grains",
            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            85: "Slight snow showers",
            86: "Heavy snow showers",
            95: "Thunderstorm",
            96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail"
        }
        return weather_descriptions.get(code, "Unknown")
    
    def display_weather(self, weather_data, city_name, address):
        """
        Display the weather forecast in a user-friendly format.
        Shows today and tomorrow's forecast.
        """
        if not weather_data or "daily" not in weather_data:
            print("Unable to display weather data.")
            return
        
        daily_data = weather_data["daily"]
        
        print("\n" + "="*60)
        print(f"WEATHER FORECAST FOR {city_name.upper()}")
        print(f"Location: {address}")
        print("="*60 + "\n")
        
        # Show forecast for today and tomorrow
        for i in range(min(2, len(daily_data["time"]))):
            date = datetime.strptime(daily_data["time"][i], "%Y-%m-%d")
            day_name = date.strftime("%A, %B %d, %Y")
            
            temp_max = daily_data["temperature_2m_max"][i]
            temp_min = daily_data["temperature_2m_min"][i]
            wind_speed = daily_data["wind_speed_10m_max"][i]
            weather_code = daily_data["weather_code"][i]
            weather_desc = self.interpret_weather_code(weather_code)
            
            print(f"📅 {day_name}")
            print(f"   🌡️  Temperature: {temp_max}°C (high) / {temp_min}°C (low)")
            print(f"   💨 Wind Speed: {wind_speed} km/h")
            print(f"   🌤️  Conditions: {weather_desc}")
            print()
    
    def run(self):
        """
        Main application loop.
        """
        print("\n" + "="*60)
        print("🌍 WEATHER APP")
        print("="*60)
        
        while True:
            city_input = input("\nEnter your city name (or 'quit' to exit): ").strip()
            
            if city_input.lower() == 'quit':
                print("Thank you for using Weather App! Goodbye! 👋\n")
                break
            
            if not city_input:
                print("Please enter a valid city name.")
                continue
            
            print("\nSearching for your location...")
            latitude, longitude, address = self.get_city_coordinates(city_input)
            
            if latitude is None:
                continue
            
            print("Fetching weather forecast...")
            weather_data = self.get_weather_forecast(latitude, longitude, city_input)
            
            if weather_data:
                self.display_weather(weather_data, city_input, address)
            else:
                print("Failed to retrieve weather data. Please try again.")
            
            time.sleep(1)  # Brief pause between requests


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
