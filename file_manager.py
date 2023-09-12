import os
import json

def check_file(file):
    if not os.path.exists(file):
            data = {"persons": []}
            with open(file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent =4)

class Manager:
    def __init__(self) -> None:
         self.persons = None
         self.brand = None
         self.plate = None
         self.kilometer = None
         self.veri = str
         self.dosya_yolu = 'persons.json'
         check_file(self.dosya_yolu)
         with open(self.dosya_yolu, 'r', encoding='utf-8') as file:
            self.veri = json.load(file)
            self.persons = self.veri.get('persons', [])
      
    def get_cars(self, person_name):
        vehicles = []

        with open(self.dosya_yolu, 'r', encoding='utf-8') as file:
            self.veri = json.load(file)
            self.persons = self.veri.get('persons', [])
            self.brand = self.veri.get('cars', [])
        
        for person in self.persons:
            if person_name == person.get('person'):
                cars = person.get('cars', [])
                for car in cars:
                    brand = car.get('car')
                    plate = car.get('plate')
                    kilometer = car.get('kilometer')
                    owner = person.get('person')

                    car_info = {
                        "Car brand": brand,
                        "Car plate": plate,
                        "Car kilometer": kilometer,
                        "Car owner": owner 
                    }
                    vehicles.append(car_info)        
        return vehicles
    
    def addCartoPerson(self, person_name, brand, plate, kilometer):
        new_car_info = {
            "car": brand,
            "kilometer": kilometer,
            "plate": plate,
        }

        for person in self.persons:
            if person_name == person.get('person'):
                cars = person.get('cars', [])
                
                for car in cars:
                    if plate == car.get('plate'):
                        print(f"Plate number {plate} already exists for {person_name}")
                        break
                else:
                    person['cars'].append(new_car_info)
                break   
                
        else:
            new_person = {
            "person": person_name,
            "cars": [new_car_info]
        }
            self.persons.append(new_person)
            
        self.veri['persons'] = self.persons
        with open(self.dosya_yolu, 'w', encoding='utf-8') as file:
            json.dump(self.veri, file, indent=4)

    def km_update(self, person_name, plate, new_km):
        for person in self.persons:
            if person_name == person.get('person'):
                cars = person.get('cars', [])

                for car in cars:
                    if plate == car.get('plate'):
                        old_km = car.get('kilometer')
                        if new_km >= old_km:
                            car['kilometer'] = new_km
                        else:
                            print("New kilometer cannot be less than older kilometer.")
                        break
                break

        self.veri['persons'] = self.persons
        with open(self.dosya_yolu, 'w', encoding='utf-8') as file:
            json.dump(self.veri, file, indent=4)    
