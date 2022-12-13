from kafka import KafkaConsumer
import logging
import os
import json
from sqlalchemy import create_engine

kafka_url = os.environ["KAFKA_URL"]
kafka_topic = os.environ["KAFKA_TOPIC"]
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

logging.info('connecting to kafka ', kafka_url)
logging.info('connecting to kafka topic ', kafka_topic)
consumer = KafkaConsumer(kafka_topic, bootstrap_servers=[kafka_url])

def insert_locationdata(locationdata):
    conn = create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
    cur = conn.cursor()
    user_id = int(locationdata["userId"])
    latitude, longitude = int(locationdata["latitude"]), int(locationdata["longitude"])
    table_insert = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))" \
        .format(user_id, latitude, longitude)

    print(table_insert)
    cur.execute(table_insert)


for message in consumer:
    print (message)

