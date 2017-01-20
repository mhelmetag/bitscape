FROM python:2.7-slim

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD . /app

EXPOSE 8080

CMD ["gunicorn", "config.wsgi", "-b", "0.0.0.0:8080", "--log-file", "-", "--access-logfile", "-", "--workers", "4"]
