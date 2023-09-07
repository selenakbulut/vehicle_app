from __future__ import print_function

import logging

import grpc
import sys
sys.path.append("..")
import com_pb2
import com_pb2_grpc

def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = com_pb2_grpc.HaberlesmeStub(channel)
        person_reply = stub.getCars(com_pb2.NameRequest(name= "engin"))
        car = person_reply.cars 
        for car in person_reply.cars:
            print("Kisinin arabasi: " + car.brand)
            print("Arabanin plakasi: " + car.plate)
            print("Arac kilometresi: " + str(car.kilometer))
            print("Arac sahibi: " + car.owner)
            print()
        
        personRes= stub.addPerson(com_pb2.Car(brand= "toyota", plate= "35KK57", kilometer=88833, owner="mert"))
        print(personRes.name)
 
if __name__ == "__main__":
    logging.basicConfig()
    run()