SECRET_KEY = "WeAreFriends_123!"
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://team3-2:Team3-2%21@redshift:5432/dev'

from flask_appbuilder.security.manager import AUTH_DB
from flask_cors import CORS

# 로그아웃한 사용자의 superset 접근 허용
PUBLIC_ROLE_LIKE = "Public" # public 권한 부여

# OAuth 사용자에게 public 역할 할당
AUTH_ROLE_PUBLIC = "Public"

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = False

# 기능 설정
DEFAULT_FEATURE_FLAGS = {
  # 대시보드에 역할 접근 허용
  "DASHBOARD_RBAC": True,  # it's obligatory
  "ENABLE_IFRAME_EMBED": True,  # 아이프레임 사용 허용
}

CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': [
        'http://localhost:8088',  # Superset
        'http://localhost:8000',  # Django
    ]
}
ENABLE_CORS = True

AUTH_TYPE = AUTH_OAUTH
