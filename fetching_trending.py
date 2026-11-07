import requests
url = "https://api.sleeper.app/v1/players/nfl/trending/add?lookback_hours=24&limit=10"
response = requests.get(url)
print(response.status_code)
print(response.json())
