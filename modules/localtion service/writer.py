import grpc
import location_pb2_grpc
import location_pb2

print("sending sample payload")

channel = grpc.insecure_channel("localhost:5006")
stub = location_pb2_grpc.Location_ServiceStub(channel)

# Update this with desired payload
item = location_pb2.LocationtMessage(
    userId=2,
    latitude=10,
    longitude=4
)

response = stub.Create(item)
print(response)