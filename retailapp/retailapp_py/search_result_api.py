import requests

url = "http://127.0.0.1:8000/retailapp/api/get-small-category"
params = {
    "gender": "F",
    "largeCategory": "상의",
    "middleCategory": "셔츠",
    "platform": "29cm"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Failed: {response.status_code}, {response.text}")
