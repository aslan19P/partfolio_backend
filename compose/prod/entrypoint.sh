python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn portfolio_backend.wsgi:application --bind 0.0.0.0:8003 --workers 4 --timeout 120 --forwarded-allow-ips="*" --log-level debug --access-logfile -
