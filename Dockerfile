FROM python:3.7
MAINTAINER Valerio Uberti "valerio.uberti23@gmail.com"
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD FLASK_ENV=development FLASK_APP=app/app.py flask run --host=0.0.0.0