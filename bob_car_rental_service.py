class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Rental Price per Day: ${self.rental_price_per_day}")
    def calculate_rental_cost(self,days):
        return days * self.rental_price_per_day
    # Getter & Setter
    def get_rental_price(self):
        return self.__rental_price_per_day
    def set_rental_price(self,price):
        self.__rental_price_per_day = price
        
class Car(Vehicle):
    def __init__(self,brand,model,year,rental_price_per_day,seating_capacity):
        super().__init__(brand,model,year,rental_price_per_day)
        self.seating_capacity = seating_capacity

    def display_info(self):
        return print(f"Car :{self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self.get_rental_price()}/day")

class Bike(Vehicle):
    def __init__(self,brand,model,year,rental_price_per_day,engine_capacity):
        super().__init__(brand,model,year,rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        return print(f"Bike :{self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price: ${self.get_rental_price()}/day")

class Client: 
    def __init__(self,name,phone,car,days,total_price):
        self.name = name
        self.phone = phone
        self.car = car
        self.days = days
        self.total_price = total_price

    def display_info(self):
        print(f"=> Client Name: {self.name} ,PhoneNumber: {self.phone}, Rented: {self.car} for {self.days} days")
    
# Calculate rental costs for a given number of days
def display_rent(v,days):
    print(f"Rental cost for {v.brand} {v.model} for {days} days: ${days*v.get_rental_price()}")


def modify(v,new):
    v.set_rental_price(new)
    print(f"Updated rental price for {v.brand} {v.model}: ${v.get_rental_price()}/day")

clients = []  # store our clients

# Selection
def selectionProcess(cars, selected):
    if selected:
                print("===========================")
                print(f"You selected {selected.brand} {selected.model} {selected.year} for ${selected.get_rental_price()}/day")
                print("===========================")
                days = int(input("Enter how many days you want to rent it: "))
                while days <=0:
                    days = int(input("You need to rent it at least for 1 day. Enter number of days: "))
                print("===========================")
                display_rent(selected,days)
                agree = input(f"Are you sure you want to rent this vehicle? [(Y)for YES (N)for NO]:")
                if agree[0].lower() == "y":
                    total = selected.get_rental_price()*days
                    car = f"{selected.brand} {selected.model} {selected.year}"
                    printReceipt(car,days,total)
                    removeVehicle(cars,selected)
                    action =None
                else:
                    action ="5"

# Print the final receipt details + adding client to client list
def printReceipt(car,days,price):
    name = input("Please enter your Full Name: ")
    phone = input("Please enter your Phone Number: ")
    print("###############")
    print("Car Rent Receipt: \n")
    print(f"Mr/Mrs.{name}\nRented: {car}\nDuration: {days} days.")
    print(f"Phone Number: {phone}.\n")
    print("-------------------")
    print(f"Total Rental Price: ${price}")
    print("###############")

    

# Viewing vehicles available and letting user to choose 
def viewVehicle(type,flag):
    if len(type)!=0:
        print("\nAvailable:")
        print("-------------------")
        i = 1
        for vehicle in type:
            print(f"{i}.",end=" ")# print on same line
            vehicle.display_info()
            i+=1
        if flag == 0:
            return None
        selected = int(input("\nSelect car number you want: ")) - 1 
        if selected == -1:
            return None
        elif 0<= selected <len(type):
            return type[selected]
    else: # list empty
        print("\nNo more available vehicles right now please come back later!!")
        print("-----------------------------")
    
# Remove from available list
def removeVehicle(type,selected):
    type.remove(selected)

def prompt():
    print("\nWELCOME To Bob's Rental Service!!!\n")
    print("Enter 1 to view available cars")
    print("Enter 2 to view available bikes")
    print("Enter \"admin\" for admin only")
    print("Enter 5 to exit")
    return input("Choice: ").strip()


# Admin dict 
admin_dict  = {
    "user_name" : "admin123",
    "password" : "123admin"
}

def admin_prompt():
    print("\nWELCOME Admin:")
    print("---------------")
    print("Enter 1 to add new vehicle: ")
    print("Enter 2 to modify vehicle price: ")
    print("Enter 3 to view clients' list: ")
    print("Enter 5 to exit admin mode: ")
    return input("Choice: ").strip()[0]

def addVehicle(type,symbol):
    #brand,model,year,rental_price_per_day,seating_capacity)
    brand = input("Enter Brand Name: ")
    model = input("Enter Model Name: ")
    year = input("Enter Year: ")
    rental_price_per_day = int(input("Enter Price/Day: "))
    if symbol == "c":
        seating_capacity = input("Enter Seating Capacity: ")
        car = Car(brand,model,year,rental_price_per_day,seating_capacity)
        cars.append(car)
    elif symbol == "b":
        engine_capacity = input("Enter Engine Capacity: ")
        bike = Bike(brand,model,year,rental_price_per_day,engine_capacity)
        bikes.append(bike)

# Admin validation
def validation():
    name = input("Enter username: ").strip()
    password = input("Enter your password: ").strip()
    if (name == admin_dict["user_name"] and password == admin_dict["password"]):
        while True:
            action = admin_prompt()
            if action =="5":
                break
            if action == "1":
                vehicle = input("What type of vehilce:\n(1) for Cars | (2) for Bikes: ").strip()[0]
                while int(vehicle) > 2:
                    vehicle = input("Enter a valid option: 1 Or 2 ").strip()[0]
                if vehicle == "1":
                    addVehicle(cars,"c")
                    viewVehicle(cars,0)
                    print("Successfully Added!!!")
                elif vehicle == "2":
                    addVehicle(bikes,"b")
                    viewVehicle(bikes,0)
                    print("Successfully Added!!!")
            elif action =="2":
                vehicle = input("What type of vehilce:\n(1) for Cars | (2) for Bikes: ").strip()[0]
                while int(vehicle) > 2:
                    vehicle = input("Enter a valid option: 1 Or 2 ").strip()[0]
                if vehicle == "1":
                    selected = viewVehicle(cars,1)
                    new_price = int(input("Enter the new price: "))
                    modify(selected,new_price)
                    print("Price modified!!!")
                elif vehicle == "2":
                    selected = viewVehicle(bikes,1)
                    new_price = int(input("Enter the new price: "))
                    modify(selected,new_price)
                    print("Price modified!!!")
                
            elif action =="3":
                displayClients()
    else:
        print("Wrong username or password !!!")
        

#  Vehicles
cars = [Car("Toyota", "Corolla", 2020, 50, 5),Car("Nissan","Sunny",2018,40,5)]
bikes = [Bike("Yamaha", "R1", 2019, 30, 998)]

# Program inputs and results
action = None
while action != "5":
    action = prompt()
    match action:  # there is no switch case in python
        case "1" :
            selected = viewVehicle(cars,1)
            selectionProcess(cars, selected)
        case "2":
            selected = viewVehicle(bikes,1)
            selectionProcess(bikes, selected)
        case "admin":
            validation()

print("\nDrive Safe, Bye!!!\n")