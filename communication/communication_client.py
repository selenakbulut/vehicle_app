from __future__ import print_function

import grpc
import sys
sys.path.append("..")
import com_pb2
import com_pb2_grpc


class MyClient:
    def __init__(self, endpoint):
        self.channel = grpc.insecure_channel(endpoint)
        self.stub = com_pb2_grpc.CommunicationStub(self.channel)
    
    def get_cars(self, person_name):
        request = com_pb2.NameRequest(name=person_name)
        personReply = self.stub.getCars(request)
        return personReply.cars
    
    def add_person (self, brand, plate, kilometer, owner):
        request = com_pb2.Car(brand=brand, plate=plate, kilometer=kilometer, owner=owner)
        personRes= self.stub.addPerson(request)
        return personRes.name
    
    def km_update (self, owner, plate, new_kilometer):
        request = com_pb2.KilometerInfo(owner=owner, plate=plate, new_kilometer=new_kilometer)
        kmRes = self.stub.kilometerUpdate(request)
        return kmRes.name 

