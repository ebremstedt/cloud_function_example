import requests


def fetch_weather_data(api_url: str, api_key: str, location: str, date: str) -> str:
    params = {
        'key': api_key,
        'q': location,
        'date': date
    }

    try:
        response = requests.get(api_url, params=params)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data from API: {e}')
