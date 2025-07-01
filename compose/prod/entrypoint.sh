python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn check_flow_backend.wsgi:application --bind 0.0.0.0:8002 --workers 4 --timeout 120 --forwarded-allow-ips="*" --log-level debug
