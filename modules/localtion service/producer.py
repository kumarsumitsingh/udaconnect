import time
from concurrent import futures
import kafka
import grpc
import location_pb2
import location_pb2_grpc
import json

TOPIC_NAME="kafka_producer_q"
KAFKA_SERVER='localhost:9092'


class locationservicer(location_pb2_grpc.Location_ServiceServicer):
    
    def Create(self,request, context):
        
        print("printing request")
        print(request)
        producer = kafka.KafkaProducer(bootstrap_servers=KAFKA_SERVER)
        request_value={
            "userId":request.userId,
            "latitude":request.latitude,
            "longitude":request.longitude

        }

        encoded_data = json.dumps(request_value, indent=2).encode('utf-8')

        producer.send(TOPIC_NAME,encoded_data)
        
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



#Kafka
#channel = grpc.insecure_channel("localhost:5005")
#stub=location_pb2_grpc.Location_ServiceStub(channel)
#location=location_pb2.locationMessage()
#TOPIC_NAME = 'items'
#KAFKA_SERVER = 'localhost:9092'
#producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

#producer.send(TOPIC_NAME, b'Test Message!!!')
#producer.flush() 