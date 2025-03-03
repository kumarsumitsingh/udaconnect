import time
from concurrent import futures
import kafka
import grpc
import location_pb2
import location_pb2_grpc
import json
import logging
import os



kafka_url = os.environ["KAFKA_URL"]
kafka_topic = os.environ["KAFKA_TOPIC"]
logging.info('connecting to kafka ', kafka_url)
logging.info('connecting to kafka topic ', kafka_topic)

class locationservicer(location_pb2_grpc.Location_ServiceServicer):
    
    def Create(self,request, context):
        
        print("printing request")
        print(request)
        producer = kafka.KafkaProducer(bootstrap_servers=kafka_url)
        request_value={
            "userId":request.userId,
            "latitude":request.latitude,
            "longitude":request.longitude

        }

        encoded_data = json.dumps(request_value, indent=2).encode('utf-8')

        producer.send(kafka_topic,encoded_data)
        
        return location_pb2.LocationtMessage(**request_value)

        

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_Location_ServiceServicer_to_server(locationservicer(), server)
print("Server starting on port 5006...")
server.add_insecure_port("[::]:5006")
server.start()
#Keep thread alive

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)


