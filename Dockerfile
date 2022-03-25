FROM python:3.9

WORKDIR /usr/src/djangoproj

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/djangoproj
RUN pip install -r /usr/src/djangoproj/requirements.txt