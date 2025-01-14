SECRET_KEY = "WeAreFriends_123!"
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://team3-2:Team3-2%21@redshift:5432/dev"


# 로그아웃한 사용자의 superset 접근 허용
PUBLIC_ROLE_LIKE = "Public"  # public 권한 부여

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

ENABLE_PROXY_FIX = True
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = False
WTF_CSRF_ENABLED = False
