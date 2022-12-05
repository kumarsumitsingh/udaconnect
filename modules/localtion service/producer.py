import time
from concurrent import futures
from kafka import KafkaProducer
import grpc
import location_pb2
import location_pb2_grpc



channel = grpc.insecure_channel("localhost:5005")
stub=location_pb2_grpc.Location_ServiceStub(channel)

"""Please review line#15 as location_pb2 is not showing location message"""
"""I also checked pb2 file and it doesnt look good"""
location=location_pb2.
TOPIC_NAME = 'items'
KAFKA_SERVER = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(TOPIC_NAME, b'Test Message!!!')
producer.flush() 