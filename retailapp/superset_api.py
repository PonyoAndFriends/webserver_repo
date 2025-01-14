import requests

def get_superset_token(base_url, username, password):
    """
    Superset에서 API 토큰을 요청합니다.

    :param base_url: Superset 서버 URL (예: "http://your-superset-url")
    :param username: Superset 사용자 이름
    :param password: Superset 비밀번호
    :return: JWT 토큰 문자열
    """
    login_url = f"{base_url}/api/v1/security/login"
    payload = {"username": username, "password": password}

    response = requests.post(login_url, json=payload)

    if response.status_code == 200:
        token = response.json().get("access_token")
        print("[INFO] 토큰 요청 성공")
        return token
    else:
        print("[ERROR] 토큰 요청 실패:", response.json())
        return None

def fetch_dashboard_data(base_url, token, dashboard_id):
    """
    Superset 대시보드 데이터를 가져옵니다.

    :param base_url: Superset 서버 URL
    :param token: JWT 토큰 문자열
    :param dashboard_id: 대시보드 ID
    :return: 대시보드 데이터 JSON
    """
    dashboard_url = f"{base_url}/api/v1/dashboard/{dashboard_id}"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(dashboard_url, headers=headers)

    if response.status_code == 200:
        print("[INFO] 대시보드 데이터 요청 성공")
        return response.json()
    else:
        print("[ERROR] 대시보드 데이터 요청 실패:", response.json())
        return None

if __name__ == "__main__":
    # Superset 서버 URL 및 사용자 정보 설정
    BASE_URL = "http://localhost:8088"  # Superset 서버 URL 입력
    USERNAME = "admin"  # 사용자 이름 입력
    PASSWORD = "admin"  # 비밀번호 입력

    # 대시보드 ID 설정
    DASHBOARD_ID = "2"  # 가져올 대시보드의 ID 입력

    # 1. 토큰 요청
    token = get_superset_token(BASE_URL, USERNAME, PASSWORD)

    if token:
        # 2. 대시보드 데이터 요청
        dashboard_data = fetch_dashboard_data(BASE_URL, token, DASHBOARD_ID)

        if dashboard_data:
            print("대시보드 데이터:", dashboard_data)
