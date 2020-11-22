import grpc
import definition_pb2
import definition_pb2_grpc

def main():
  with grpc.insecure_channel('localhost:50051') as channel:
    stub = definition_pb2_grpc.ServerStub(channel)
    response = stub.RemoteFunction(definition_pb2.Request(content="test"))
  print("Recieved:", response.content)

if __name__ == '__main__':
  main()