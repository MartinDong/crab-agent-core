
"""
Weather Skill Module

Provides weather query functionality using Amap (高德地图) weather API.
"""

import os
import requests
from typing import Optional, Dict, Any
from dotenv import load_dotenv

load_dotenv()


class WeatherSkill:
    """
    Weather Skill class for querying weather information.
    
    This skill provides real-time weather and weather forecast queries.
    It supports both real API calls and mock data for development.
    
    Example:
        skill = WeatherSkill()
        weather = skill.execute("北京")
        print(weather)
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the weather skill.
        
        Args:
            api_key: Amap API key. If not provided, reads from AMAP_WEATHER_KEY env var.
        """
        self.api_key = api_key or os.getenv("AMAP_WEATHER_KEY", "c1b86d99ce6fee8bb9e1f6313e18297c")
        self.base_url = "https://restapi.amap.com/v3/weather/weatherInfo"
        
        if not self.api_key:
            print("Warning: No Amap API key configured, using mock data")
    
    def get_weather(self, city: str, extensions: str = "base"):
        """
        Query weather information.
        
        Args:
            city: City name or adcode
            extensions: Query type
                - "base": Real-time weather (default)
                - "all": Weather forecast
        
        Returns:
            Weather data dictionary
        """
        if not self.api_key:
            return self._get_mock_weather(city, extensions)
        
        try:
            params = {
                "key": self.api_key,
                "city": city,
                "extensions": extensions,
                "output": "json"
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            result = response.json()
            
            if result.get("status") == "1":
                return result
            else:
                return {
                    "status": "0",
                    "info": result.get("info", "Query failed"),
                    "infocode": result.get("infocode", "")
                }
        
        except Exception as e:
            return {
                "status": "0",
                "info": f"Request error: {str(e)}",
                "infocode": "9999"
            }
    
    def _get_mock_weather(self, city: str, extensions: str = "base"):
        """
        Get mock weather data (used when no API key is available).
        
        Args:
            city: City name
            extensions: Query type
        
        Returns:
            Mock weather data
        """
        mock_data = {
            "北京": {
                "weather": "晴",
                "temperature": "22",
                "wind_direction": "东北",
                "wind_power": "3",
                "humidity": "45"
            },
            "上海": {
                "weather": "多云",
                "temperature": "25",
                "wind_direction": "东南",
                "wind_power": "2",
                "humidity": "65"
            },
            "广州": {
                "weather": "阵雨",
                "temperature": "28",
                "wind_direction": "南",
                "wind_power": "2",
                "humidity": "75"
            },
            "深圳": {
                "weather": "阴",
                "temperature": "27",
                "wind_direction": "西南",
                "wind_power": "3",
                "humidity": "70"
            }
        }
        
        city_data = mock_data.get(city, {
            "weather": "晴",
            "temperature": "20",
            "wind_direction": "东",
            "wind_power": "2",
            "humidity": "50"
        })
        
        if extensions == "base":
            return {
                "status": "1",
                "count": "1",
                "info": "OK",
                "infocode": "10000",
                "lives": [
                    {
                        "province": city,
                        "city": city,
                        "adcode": "110000",
                        "weather": city_data["weather"],
                        "temperature": city_data["temperature"],
                        "winddirection": city_data["wind_direction"],
                        "windpower": city_data["wind_power"],
                        "humidity": city_data["humidity"],
                        "reporttime": "2024-01-01 12:00:00"
                    }
                ]
            }
        else:
            return {
                "status": "1",
                "count": "1",
                "info": "OK",
                "infocode": "10000",
                "forecasts": [
                    {
                        "city": city,
                        "adcode": "110000",
                        "province": city,
                        "reporttime": "2024-01-01 12:00:00",
                        "casts": [
                            {
                                "date": "2024-01-01",
                                "week": "1",
                                "dayweather": city_data["weather"],
                                "nightweather": "多云",
                                "daytemp": city_data["temperature"],
                                "nighttemp": "15",
                                "daywind": city_data["wind_direction"],
                                "nightwind": city_data["wind_direction"],
                                "daypower": city_data["wind_power"],
                                "nightpower": city_data["wind_power"]
                            }
                        ]
                    }
                ]
            }
    
    def format_weather(self, weather_data):
        """
        Format weather data into readable text.
        
        Args:
            weather_data: Weather data from get_weather()
        
        Returns:
            Formatted weather information
        """
        if weather_data.get("status") != "1":
            return f"Error: Weather query failed: {weather_data.get('info', 'Unknown error')}"
        
        if "lives" in weather_data:
            lives = weather_data["lives"][0]
            return (
                f"Weather in {lives['city']}\n"
                f"====================\n"
                f"Report time: {lives['reporttime']}\n"
                f"Weather: {lives['weather']}\n"
                f"Temperature: {lives['temperature']} deg C\n"
                f"Wind: {lives['winddirection']} wind, {lives['windpower']} level\n"
                f"Humidity: {lives['humidity']}%"
            )
        elif "forecasts" in weather_data:
            forecast = weather_data["forecasts"][0]
            result = f"Forecast for {forecast['city']}\n"
            result += "====================\n"
            result += f"Report time: {forecast['reporttime']}\n\n"
            
            for cast in forecast["casts"]:
                result += (
                    f"{cast['date']} (Week {cast['week']}):\n"
                    f"  Day: {cast['dayweather']}, {cast['daytemp']} deg C, {cast['daywind']} wind {cast['daypower']} level\n"
                    f"  Night: {cast['nightweather']}, {cast['nighttemp']} deg C, {cast['nightwind']} wind {cast['nightpower']} level\n\n"
                )
            return result
        else:
            return "Unknown weather data format"
    
    def execute(self, city: str, extensions: str = "base"):
        """
        Unified execution interface for Agent invocation.
        
        Args:
            city: City name
            extensions: Query type ("base" or "all")
        
        Returns:
            Formatted weather information
        """
        weather_data = self.get_weather(city, extensions)
        return self.format_weather(weather_data)
