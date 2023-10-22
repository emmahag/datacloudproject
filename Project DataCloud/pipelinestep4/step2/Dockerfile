FROM python:3.8

WORKDIR /app

COPY . ./

RUN pip install paho-mqtt

ENV NAME World

CMD ["python", "step2.py"]
