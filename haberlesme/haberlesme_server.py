from concurrent import futures
import logging

import grpc

import os 
import json

import com_pb2
import com_pb2_grpc

class Haberlesme(com_pb2_grpc.HaberlesmeServicer):
    def __init__(self) -> None:
        self.kisiler = None
        self.brand = None
        self.plate = None
        self.kilometer = None
        self.veri = str
        self.dosya_yolu = 'kisiler.json'
        with open('kisiler.json', 'r', encoding='utf-8') as file:
            self.veri = json.load(file)
            self.kisiler = self.veri.get('kisiler', [])
    
    def showCar(self, request, context):
        with open(self.dosya_yolu, 'r', encoding='utf-8') as file:
             self.veri = json.load(file)
             self.kisiler = self.veri.get('kisiler', [])
             self.brand = self.veri.get('arabalar', [])
        
        car = com_pb2.Car()
        for kisi in self.kisiler:
            if request.name == kisi.get('kisi'):
                arabalar = kisi.get('arabalar', [])
                for araba in arabalar:
                    car.plate = araba.get('plaka')
                    car.brand = araba.get('araba')
                    car.kilometer = araba.get('kilometre')
                    car.owner = kisi.get('kisi')
        return car
    
    def getCars(self, request, context):
        with open(self.dosya_yolu, 'r', encoding='utf-8') as file:
             self.veri = json.load(file)
             self.kisiler = self.veri.get('kisiler', [])
             self.brand = self.veri.get('arabalar', [])

        person = com_pb2.PersonReply()
        for kisi in self.kisiler:
            if request.name == kisi.get('kisi'):
                arabalar = kisi.get('arabalar', [])
                for araba in arabalar:
                    new_car = com_pb2.Car()
                    new_car.brand = araba.get('araba')
                    new_car.plate = araba.get('plaka')
                    new_car.kilometer = araba.get('kilometre')
                    new_car.owner = kisi.get('kisi')
                    person.cars.append(new_car)
                    
        return person

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