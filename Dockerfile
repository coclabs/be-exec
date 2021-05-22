FROM python:3.9.5-alpine3.12

WORKDIR /srv/exec-services/python-exec-service

COPY . .

RUN pip3.9.5 install -r requirements.txt -c requirements.txt

CMD ['--reload']
ENTRYPOINT ['uvicorn', 'main:App.service']