FROM python:3.9-alpine

WORKDIR .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["python","location-consumer.py"]