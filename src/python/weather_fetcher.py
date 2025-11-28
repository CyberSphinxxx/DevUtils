import requests

def get_weather(city, api_key):
    """
    Fetches weather data for a city using OpenWeatherMap API.
    Note: Requires a valid API key.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Error {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Placeholder API key
    api_key = "YOUR_API_KEY_HERE"
    city = "London"
    print(f"Fetching weather for {city}...")
    # print(get_weather(city, api_key)) 
    print("Please provide a valid API key to run this script.")
