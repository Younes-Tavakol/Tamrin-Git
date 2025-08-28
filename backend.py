import requests

API_KEY = "d23b62346dbaf87f4a1218a6ea493b53"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

ojenhfO;kjn
if __name__=="__name__":
    print(get_data(place="Tokyo", forecast_days=3))