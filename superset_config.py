# superset_config.py

# 1. Bật các tính năng cần thiết
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "ENABLE_JAVASCRIPT_CONTROLS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "PRESTO_EXPAND_DATA": True,
    "DASHBOARD_RBAC": True
}

# 2. Cấu hình CORS đúng cách cho embedded mode
ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': ['*'],
    'expose_headers': ['*'],
    'methods': ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH']
}

ENABLE_PROXY_FIX = True
# 3. Tắt CSRF protection cho embedded mode
WTF_CSRF_ENABLED = False
TALISMAN_ENABLED = False

# 4. Cấu hình cookie đúng cách cho cross-origin embedding
SESSION_COOKIE_SAMESITE = None  # Quan trọng: None thay vì 'None'
SESSION_COOKIE_SECURE = False   # Để False vì đang dùng HTTP (không phải HTTPS)
SESSION_COOKIE_HTTPONLY = False # Cho phép JavaScript truy cập cookie
SESSION_COOKIE_DOMAIN = None    # Không giới hạn domain

# 5. Cấu hình thêm cho embedded mode
# Cấu hình vai trò công khai (Public role)
PUBLIC_ROLE_LIKE = "Gamma"  # Gán quyền tương tự vai trò Gamma (hoặc vai trò khác tùy nhu cầu)
GUEST_ROLE_NAME = "Public"  # Vai trò cho người dùng không đăng nhập
#GUEST_ROLE_NAME = "Gamma"       # Role mặc định cho guest users
GUEST_TOKEN_JWT_SECRET = "8a4874f964ef529cbb71fdabe2753d2f8c0771353e2e70eeafc2fac3e7f33c53"  # Secret key cho JWT token
GUEST_TOKEN_JWT_ALGO = "HS256"  # Algorithm cho JWT
GUEST_TOKEN_HEADER_NAME = "X-GuestToken"  # Header name cho guest token

# 6. Cấu hình headers cho phép nhúng
HTTP_HEADERS = {
    'X-Frame-Options': 'ALLOWALL',
    'Content-Security-Policy': "frame-ancestors 'self' *; default-src 'self' 'unsafe-inline' 'unsafe-eval' *;",
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS, PATCH',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-GuestToken, X-Requested-With',
    'Access-Control-Allow-Credentials': 'true'
}

# 7. Cấu hình để xử lý guest token trong embedded views
GUEST_TOKEN_JWT_EXP_SECONDS = 3600  # Token hết hạn sau 5 phút

# 8. Logging để debug
import logging
logging.getLogger('superset.security').setLevel(logging.DEBUG)
logging.getLogger('superset.views').setLevel(logging.DEBUG)
