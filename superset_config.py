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

# superset_config.py
from flask_appbuilder.security.manager import AUTH_DB
# AUTH_TYPE을 PUBLIC으로 설정
from flask_appbuilder.security.manager import AUTH_OID

# AUTH_TYPE = AUTH_DB
AUTH_TYPE = AUTH_OID  # OpenID 기반 인증 사용

# Remove or customize the X-Frame-Options header
CUSTOM_SECURITY_MANAGER = None
WTF_CSRF_ENABLED = False  # Optional if you are testing

  # Dashboard embedding
GUEST_ROLE_NAME = "Gamma"
# 게스트 계정을 익명 사용자로 설정
PUBLIC_ROLE_LIKE = "Gamma"  # 읽기 전용 역할 부여

GUEST_TOKEN_JWT_SECRET = "test-guest-secret-change-me"
GUEST_TOKEN_JWT_ALGO = "HS256"
GUEST_TOKEN_HEADER_NAME = "X-GuestToken"
GUEST_TOKEN_JWT_EXP_SECONDS = 300
TALISMAN_ENABLED = False
ENABLE_CORS = True
HTTP_HEADERS={"X-Frame-Options":"ALLOWALL"}



# 로그인을 요구하지 않도록 설정
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Public"  # 기본 Public 권한으로 설정