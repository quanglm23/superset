#!/bin/bash
# Dừng ngay lập tức nếu có lỗi
set -e

echo ">>> [BOOTSTRAP] BAT DAU CAI DAT TUY CHINH..."

# Bước này cần quyền root. Image Superset mặc định khởi động với quyền root
# trước khi chuyển sang user 'superset'.
echo ">>> [BOOTSTRAP] Kiem tra quyen root và cai dat goi he thong..."
apt-get update && apt-get install -y --no-install-recommends curl gnupg unixodbc-dev

# Cài đặt MS ODBC Driver (theo cách mới nhất)
curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/11/prod bullseye main" > /etc/apt/sources.list.d/mssql-release.list
apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18

# Cài đặt gói Python. Lệnh này có thể chạy bởi user 'superset'
echo ">>> [BOOTSTRAP] Cai dat goi Python pyodbc..."
pip install pyodbc

echo ">>> [BOOTSTRAP] Hoan tat cai dat tuy chinh. Chay entrypoint goc..."

# Dùng 'exec' để chạy tiến trình Superset gốc.
# Điều này đảm bảo Superset trở thành tiến trình chính của container.
exec /app/docker/docker-entrypoint.sh
