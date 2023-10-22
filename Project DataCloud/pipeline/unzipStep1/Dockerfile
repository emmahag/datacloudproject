FROM python:3.8

WORKDIR /app

COPY . ./

RUN pip install pika

ENV NAME World

CMD ["python", "unzipStep1.py"]
