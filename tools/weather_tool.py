import httpx

def get_weather_by_coords(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
    r = httpx.get(url, timeout=10)
    return r.json()
