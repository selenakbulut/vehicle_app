import logging
from communication import communication_client

def menu():
    while True:
        print("\nWhat do you want to do: ")
        print("1- Show cars information")
        print("2- Add new person")
        print("3- Update kilometer information")
        print("4- Exit")

        choice= input("Enter your choice: ")

        c = communication_client.MyClient("localhost:50051")
        if choice == "1":
            p_name = input("Write your name: ").lower()
            resp = c.get_cars(person_name=p_name)
            for car in resp:
                print("Person's car: " + car.brand)
                print("Plate of the car: " + car.plate)
                print("Kilometer of the car: " + str(car.kilometer))
                print("Car owner: " + car.owner)
                print()
        
        elif choice == "2":
            brand = input("Write a car brand: ")
            plate = input("Write a car plate: ")
            kilometer = int(input("Write a car kilometer: "))
            owner = input("Write a name that you want to add: ")
            c.add_person(brand=brand, plate=plate, kilometer=kilometer, owner=owner)
        
        elif choice == "3":
            owner = input("Enter car owner: ")
            plate = input("Enter car plate you want to reach: ")
            new_kilometer = int(input("Enter new kilometer: "))
            c.km_update(owner=owner, plate=plate, new_kilometer=new_kilometer)
        
        else:
            break

if __name__ == "__main__":
    logging.basicConfig()
    menu()