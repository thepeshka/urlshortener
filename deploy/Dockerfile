FROM python:3.6

WORKDIR /app

COPY ./deploy/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./src /app

COPY ./deploy/run.sh /run.sh

ENTRYPOINT /run.sh
