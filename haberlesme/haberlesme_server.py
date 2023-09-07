from concurrent import futures
import logging

import grpc

import sys
sys.path.append("..")
import com_pb2
import com_pb2_grpc
import file_manager


class Haberlesme(com_pb2_grpc.HaberlesmeServicer):
    
    def getCars(self, request, context):

        person = com_pb2.CarReply()
        man = file_manager.Manager()

        data = man.get_cars(person_name=request.name)
        
        for kisi in data:
            new_car = com_pb2.Car()
            new_car.brand = kisi.get('Arac markasi')
            new_car.plate = kisi.get('Arac plakasi')
            new_car.kilometer = kisi.get('Arac kilometresi')
            new_car.owner = kisi.get('Arac sahibi')
            person.cars.append(new_car)
        return person
    
    def addPerson(self, request, context):
        resp = com_pb2.PersonResponse()
        man = file_manager.Manager()
        resp.name = request.owner

        man.addCartoPerson(person_name=request.owner,brand=request.brand, plate=request.plate, kilometer=request.kilometer )
        return resp
    
def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    com_pb2_grpc.add_HaberlesmeServicer_to_server(Haberlesme(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()