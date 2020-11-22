from concurrent import futures
import grpc
import definition_pb2
import definition_pb2_grpc

class Server(definition_pb2_grpc.Server):
  def RemoteFunction(self, request, _context):
    return definition_pb2.Reply(content=2*request.content)

def main():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
  definition_pb2_grpc.add_ServerServicer_to_server(Server(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()

if __name__ == '__main__':
  main()