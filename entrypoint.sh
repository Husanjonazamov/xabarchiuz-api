python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput

uvicorn config.asgi:application --host 0.0.0.0 --port 8000 --reload

exit $?


