FROM python:3.9.17-alpine3.17


ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SUPERUSER_PASSWORD root

WORKDIR /ecommerce

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . /ecommerce
