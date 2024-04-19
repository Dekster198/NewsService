FROM python:latest
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /newsservice
COPY requirements.txt /newsservice/
RUN pip install -r requirements.txt
COPY . /newsservice/