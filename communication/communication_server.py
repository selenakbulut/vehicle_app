from concurrent import futures
import logging

import grpc

import sys
sys.path.append("..")
import com_pb2
import com_pb2_grpc
import file_manager


class Communication(com_pb2_grpc.CommunicationServicer):
    
    def getCars(self, request, context):

        rep = com_pb2.CarReply()
        man = file_manager.Manager()

        data = man.get_cars(person_name=request.name)
        
        for person in data:
            new_car = com_pb2.Car()
            new_car.brand = person.get('Car brand')
            new_car.plate = person.get('Car plate')
            new_car.kilometer = person.get('Car kilometer')
            new_car.owner = person.get('Car owner')
            rep.cars.append(new_car)
        return rep
    
    def addPerson(self, request, context):
        resp = com_pb2.PersonResponse()
        man = file_manager.Manager()
        resp.name = request.owner

        man.addCartoPerson(person_name=request.owner,brand=request.brand, plate=request.plate, kilometer=request.kilometer)
        return resp
    
    def kilometerUpdate(self, request, context):
        response = com_pb2.PersonResponse()
        man = file_manager.Manager()
        response.name = "engin"
       
        man.km_update(person_name=request.owner, plate=request.plate, new_km=request.new_kilometer)
        return response
    
def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    com_pb2_grpc.add_CommunicationServicer_to_server(Communication(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()