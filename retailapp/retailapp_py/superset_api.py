import os
import requests

SUPERSET_BASE_URL = "http://localhost:8088"
SUPERSET_LOGIN_API = f"{SUPERSET_BASE_URL}/api/v1/security/login"
SUPERSET_CHART_API = f"{SUPERSET_BASE_URL}/api/v1/chart/"

SUPERSET_USERNAME = os.getenv("SUPERSET_USERNAME", "admin")
SUPERSET_PASSWORD = os.getenv("SUPERSET_PASSWORD", "admin")

def get_access_token():
    login_payload = {
        "username": SUPERSET_USERNAME,
        "password": SUPERSET_PASSWORD,
        "provider": "db",
    }
    try:
        response = requests.post(SUPERSET_LOGIN_API, json=login_payload)
        response.raise_for_status()
        access_token = response.json().get("access_token")
        if access_token:
            print(f"Access Token: {access_token}")
            return access_token
        else:
            print("Failed to retrieve access token.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error during login: {e}")
        return None

def fetch_specific_chart(access_token, chart_id):
    url = f"{SUPERSET_BASE_URL}/api/v1/chart/{chart_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(f"Chart Data for ID {chart_id}: {data}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching chart data for ID {chart_id}: {e}")
        return {"error": str(e)}

if __name__ == "__main__":
    token = get_access_token()
    if token:
        chart_data = fetch_specific_chart(token, chart_id=1)  # 차트 ID를 지정
        print(chart_data)
    else:
        print("Failed to get access token.")
