# km daha düşük güncellenemez
# eğer 1 tane araci varsa sormasın hangi aracin güncelleneceğini 
# kisi ekleme dediğinde o kişi zaten varsa uyarı versin ve kisi eklemesin

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

class Vehicle:
    def __init__(self) -> None:
        self.arac_marka = None
        self.plaka = None
        self.kilometre = None
        self.dosya_yolu = 'kisiler.json'
        self.veri = str
        self.kisiler = None
        with open(self.dosya_yolu, 'r', encoding='utf-8') as file:
            self.veri = json.load(file)
            self.kisiler = self.veri.get('kisiler', [])

    def kisi_ekleme(self):
        kisi_adi = input("Kişi adini giriniz: ").lower()
        for kisi in self.kisiler:
            if kisi['kisi'] == kisi_adi:
                print(f"{kisi_adi} adli kisi zaten var.")
                return
            
        kisi = {
            "kisi": kisi_adi,
            "arabalar": []
        }

        araba_sayisi = int(input("Kaç tane araba eklemek istersiniz: "))
        for _ in range(araba_sayisi):
            marka = input("Araba markasini giriniz: ")
            kilometre = int(input("Kilometreyi giriniz: "))
            plaka = input("Plakayi giriniz: ")

            araba = {
                "araba": marka,
                "kilometre": kilometre,
                "plaka": plaka
            }
            kisi['arabalar'].append(araba)

        self.kisiler.append(kisi)

        self.savetoFile()


    def km_güncelleme(self, kisi_adi, marka, yeni_km):

        for kisi in self.kisiler:
            if kisi['kisi'] == kisi_adi:
                arabalar = kisi['arabalar']

                for araba in arabalar:
                    if araba['araba'] == marka:
                        eski_km = int(araba['kilometre'])
                        if yeni_km >= eski_km:
                            araba['kilometre'] = yeni_km
                            self.savetoFile()
                            print(f"{kisi_adi}'in araci: {marka}, güncellenmis kilometre: {yeni_km}")
                        else:
                            print("Yeni kilometre eski kilometreden daha düsük olamaz. Güncelleme yapilamadi.")
                        break
                break
        

    def get_arabalar(self, kisi_adi):
        for kisi in self.kisiler:
            if kisi['kisi'] == kisi_adi:
                arabalar = kisi['arabalar']
                print()
                print(f"{kisi_adi} adli kisinin arabalari:")
    
                for araba in arabalar:
                    marka = araba.get('araba')
                    kilometre = araba.get('kilometre')
                    plaka = araba.get('plaka')
                    
                    print(f"  Araba Markasi: {marka}")
                    print(f"  Kilometre: {kilometre}")
                    print(f"  Plaka: {plaka}")
                    print()


    def savetoFile(self):
        with open(self.dosya_yolu, 'w', encoding='utf-8') as file:
                                json.dump(self.veri, file, ensure_ascii=False, indent=4)
        

def main():

    check_file()

    while True:
        print("\nNe yapmak istiyorsunuz: ")
        print("1- Kisi ekleme")
        print("2- Arac km güncelleme")
        print("3- Cikis")

        secim = input("Seciminizi giriniz: ")
        
        v = Vehicle()

        if secim == "1":
            v.kisi_ekleme()

        elif secim == "2":
            kisi_adi = input("İsminizi giriniz: ").lower()
            v.get_arabalar(kisi_adi)

            marka = input("Hangi aracin kilometresini degistirmek istersiniz: ")
            yeni_km = int(input("Yeni kilometreyi giriniz: "))
            v.km_güncelleme(kisi_adi, marka, yeni_km)

        else:
            break

if __name__ == "__main__":
    main()