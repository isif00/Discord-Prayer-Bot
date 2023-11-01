import requests

api_url = "http://api.aladhan.com/v1/calendar/2023/4"


def get_prayer_times():
    latitude = 51.508515
    longitude = -0.1254872

    query_params = {
    "latitude": latitude,
    "longitude": longitude
    }

    response = requests.get(api_url, params=query_params)

    if response.status_code == 200:
        prayer_times_data = response.json()
        
        return prayer_times_data
    else:
        return response.status_code

