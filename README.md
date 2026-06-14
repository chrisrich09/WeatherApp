# 🌍 Weather App

A simple Python weather application that provides real-time weather forecasts based on user location input.

## Features

✅ **City-based Lookup** — Enter any city name and find the closest matching location using geolocation  
✅ **Public API Integration** — Uses Open-Meteo API (free, no API key required)  
✅ **Weather Information**:
  - Current and forecasted temperature (high/low)
  - Wind speed
  - General weather conditions (sunny, rainy, snowy, cloudy, etc.)

✅ **Multi-day Forecast** — Shows weather for today and tomorrow  
✅ **User-friendly Interface** — Interactive command-line interface with clear output

## Installation

1. Clone the repository:
```bash
git clone https://github.com/chrisrich09/WeatherApp.git
cd WeatherApp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the weather app:
```bash
python weather_app.py
```

### Example Interaction:
```
============================================================
🌍 WEATHER APP
============================================================

Enter your city name (or 'quit' to exit): London
Searching for your location...
Fetching weather forecast...

============================================================
WEATHER FORECAST FOR LONDON
Location: London, England, United Kingdom
============================================================

📅 Sunday, June 15, 2025
   🌡️  Temperature: 22°C (high) / 15°C (low)
   💨 Wind Speed: 12 km/h
   🌤️  Conditions: Partly cloudy

📅 Monday, June 16, 2025
   🌡️  Temperature: 24°C (high) / 16°C (low)
   💨 Wind Speed: 10 km/h
   🌤️  Conditions: Sunny
```

## Dependencies

- **requests** — HTTP library for API calls
- **geopy** — Geolocation library for city name to coordinates conversion

## How It Works

1. User enters a city name
2. App uses `geopy` with OpenStreetMap's Nominatim service to convert the city name to latitude/longitude coordinates
3. App queries Open-Meteo API for weather data at those coordinates
4. Weather information (temperature, wind speed, conditions) is formatted and displayed
5. User can query multiple cities or type 'quit' to exit

## API Reference

- **Open-Meteo API** — https://open-meteo.com/ (Free weather API)
- **Geopy** — https://geopy.readthedocs.io/ (Geolocation library)

## License

This project is open source and available for educational purposes.
