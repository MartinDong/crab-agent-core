
---
name: "weather-skill"
description: "Provides weather query functionality using Amap API. Invoke when user asks about weather, forecasts, or temperature."
---

# Weather Skill

This skill provides weather query functionality using Amap (高德地图) weather API.

## Features

- Real-time weather query
- Weather forecast query
- Mock data support (no API key required)
- Formatted weather information output

## Installation

No installation required, the skill is already integrated into the project.

## Configuration

To use real API data, add to `.env` file:

```
AMAP_WEATHER_KEY=your_amap_api_key
```

## Usage

The skill is automatically used by the LangGraph agent when weather-related queries are detected.

### Direct Usage

```python
from skills.weather import WeatherSkill

skill = WeatherSkill()
result = skill.execute("北京")
print(result)
```

## API Reference

https://lbs.amap.com/api/webservice/guide/api-advanced/weatherinfo
