import requests
API_KEY = "9cd74ab89d6d419ead82cc94b83fa670"
url = f"https://api.weatherbit.io/v2.0/current?lat=39.688096271304325&lon=141.1645963703204&lang=ja&units=M&key={API_KEY}"
response = requests.get(url)
data = response.json()
print(data)