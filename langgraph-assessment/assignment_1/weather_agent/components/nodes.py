import requests

from components.state import WeatherAgentState
from components.config import config
from components.helper_functions import (
    classify_temperature,
    get_weather_description,
    get_greeting,
    format_local_time,
)

def fetch_location_data(state: WeatherAgentState) -> WeatherAgentState:
    try:
        response = requests.get(
            config.LOCATION_API_URL,
            timeout=config.REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        raw_data = response.json()

        location_data = {
            "city": raw_data.get("city", "Unknown"),
            "region": raw_data.get("regionName", "Unknown"),
            "country_name": raw_data.get("country", "Unknown"),
            "latitude": raw_data.get("lat", 0.0),
            "longitude": raw_data.get("lon", 0.0),
            "utc_offset": "+0000",
            "timezone": raw_data.get("timezone", "UTC"),
        }

        return {"location_data": location_data}

    except Exception as e:
        raise Exception(f"Failed to fetch location data: {e}")

def fetch_weather_data(state: WeatherAgentState) -> WeatherAgentState:
    location = state["location_data"]
    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current_weather": "true",
        "timezone": location.get("timezone", "auto")
    }
    
    try:
        response = requests.get(
            config.WEATHER_API_BASE_URL,
            params=params,
            timeout=config.REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        weather_data = response.json()
        return {"weather_data": weather_data}

    except Exception as e:
        raise Exception(f"Failed to fetch weather data: {e}")

def generate_weather_info(state: WeatherAgentState) -> WeatherAgentState:
    location = state["location_data"]
    weather_data = state["weather_data"]

    weather = weather_data["current_weather"]
    units = weather_data.get("current_weather_units", {})

    temperature = weather["temperature"]
    windspeed = weather["windspeed"]
    weather_code = weather["weathercode"]
    is_day = weather["is_day"]

    temp_unit = units.get("temperature", "°C")
    wind_unit = units.get("windspeed", "km/h")

    weather_info = f"""
{get_greeting(is_day)}, {state['name']}!

Location:
{location['city']}, {location['region']}, {location['country_name']}

Time:
{format_local_time(weather['time'], location['utc_offset'])}

Weather:
{get_weather_description(weather_code)}

Temperature:
{temperature}{temp_unit}
({classify_temperature(temperature)})

Wind:
{windspeed} {wind_unit}
"""
    return {"weather_info": weather_info.strip()}
