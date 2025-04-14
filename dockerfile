FROM python:3.12-slim

WORKDIR /lpg-survey-app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

EXPOSE 8538

HEALTHCHECK CMD curl --fail http://localhost:8538/_stcore/health
