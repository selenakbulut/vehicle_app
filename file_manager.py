import os
import json

def check_file():
    dosya_yolu = 'kisiler.json'
    if not os.path.exists('kisiler.json'):
            data = {"kisiler": []}
            with open(dosya_yolu, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent =4)
    else:
        print("json dosyasi zaten var:", dosya_yolu)

class Manager:
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
    

                        
                        
