from typing import TypedDict, Optional, Dict, Any

class WeatherAgentState(TypedDict):
    name: str
    location_data: Optional[Dict[str, Any]]
    weather_data: Optional[Dict[str, Any]]
    weather_info: Optional[str]
