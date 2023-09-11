import os
import json

def check_file(file):
    if not os.path.exists(file):
            data = {"kisiler": []}
            with open(file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent =4)

class Manager:
    def __init__(self) -> None:
         self.kisiler = None
         self.brand = None
         self.plate = None
         self.kilometer = None
         self.veri = str
         self.dosya_yolu = 'kisiler.json'
         check_file(self.dosya_yolu)
         with open(self.dosya_yolu, 'r', encoding='utf-8') as file:
            self.veri = json.load(file)
            self.kisiler = self.veri.get('kisiler', [])
      
    def get_cars(self, person_name):
        vehicles = []

        with open(self.dosya_yolu, 'r', encoding='utf-8') as file:
            self.veri = json.load(file)
            self.kisiler = self.veri.get('kisiler', [])
            self.brand = self.veri.get('arabalar', [])
        
        for kisi in self.kisiler:
            if person_name == kisi.get('kisi'):
                arabalar = kisi.get('arabalar', [])
                for araba in arabalar:
                    brand = araba.get('araba')
                    plate = araba.get('plaka')
                    kilometer = araba.get('kilometre')
                    owner = kisi.get('kisi')

                    car_info = {
                        "Arac markasi": brand,
                        "Arac plakasi": plate,
                        "Arac kilometresi": kilometer,
                        "Arac sahibi": owner 
                    }
                    vehicles.append(car_info)        
        return vehicles
    
    def addCartoPerson(self, person_name, brand, plate, kilometer):
        new_car_info = {
            "araba": brand,
            "kilometre": kilometer,
            "plaka": plate,
        }

        for kisi in self.kisiler:
            if person_name == kisi.get('kisi'):
                print(kisi.get('kisi'))
                arabalar = kisi.get('arabalar', [])
                print(arabalar)
                for araba in arabalar:
                    print(araba.get('plaka'))
                    if plate == araba.get('plaka'):
                        print(f"Plate number {plate} already exists for {person_name}")
                        break
                else:
                    kisi['arabalar'].append(new_car_info)
                break   
                
        else:
            new_person = {
            "kisi": person_name,
            "arabalar": [new_car_info]
        }
            self.kisiler.append(new_person)
            
        self.veri['kisiler'] = self.kisiler
        with open(self.dosya_yolu, 'w', encoding='utf-8') as file:
            json.dump(self.veri, file, indent=4)

    def km_update(self, person_name, plate, new_km):
        for kisi in self.kisiler:
            if person_name == kisi.get('kisi'):
                arabalar = kisi.get('arabalar', [])

                for araba in arabalar:
                    if plate == araba.get('plaka'):
                        old_km = araba.get('kilometre')
                        if new_km >= old_km:
                            araba['kilometre'] = new_km
                        else:
                            print("New kilometer cannot be less than older kilometer.")
                        break
                break

        self.veri['kisiler'] = self.kisiler
        with open(self.dosya_yolu, 'w', encoding='utf-8') as file:
            json.dump(self.veri, file, indent=4)    
