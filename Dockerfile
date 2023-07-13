FROM python:3.9.4
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --preload --bind 0.0.0.0:$PORT app:app --timeout 150