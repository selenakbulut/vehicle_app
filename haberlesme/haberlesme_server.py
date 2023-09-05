from concurrent import futures
import logging

import grpc

import os 
import json

import com_pb2
import com_pb2_grpc

def check_file():
    dosya_yolu = (r'C:\Users\Lenovo\Desktop\SPARSE\arac_uygulamasi\haberlesme\kisiler.json')
    if not os.path.exists(r'C:\Users\Lenovo\Desktop\SPARSE\arac_uygulamasi\haberlesme\kisiler.json'):
            data = {"kisiler": []}
            with open(dosya_yolu, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent =4)
    else:
        print("json dosyasi zaten var:", dosya_yolu)

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

    def sayName(self, request, context):
        return com_pb2.NameReply(message="Hello, %s!" % request.name)
    
    def showCar(self, request, context):

        # dosya_yolu = 'kisiler.json'
        # data = {"kisiler": []}
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
    check_file()
    serve()