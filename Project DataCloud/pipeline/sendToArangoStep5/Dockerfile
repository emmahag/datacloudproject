FROM python:3.8

WORKDIR /app

COPY . ./

RUN pip install pika

ENV NAME World

CMD ["python", "sendToArangoStep5.py"]
