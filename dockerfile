FROM python:3.9.13-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk update \
&& pip install --upgrade pip \
&& pip install -r ./requirements.txt

WORKDIR /app
COPY ./app /app

EXPOSE 8000

CMD ["python", "app.py"]