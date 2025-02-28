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
        return print(f"Car :{self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self.rental_price_per_day}/day")

class Bike(Vehicle):
    def __init__(self,brand,model,year,rental_price_per_day,engine_capacity):
        super().__init__(brand,model,year,rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        return print(f"Bike :{self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price: ${self.rental_price_per_day}/day")
    
car = Car("Toyota", "Corolla", 2020, 50, 5)
bike = Bike("Yamaha", "R1", 2019, 30, 998)
# Display details
car.display_info()
bike.display_info()
# Calculate rental costs for a given number of days
def display_rent(v,days):
    print(f"Rental cost for {v.brand} {v.model} for {days} days: ${days*v.get_rental_price()}")

display_rent(car,3)
display_rent(bike,7)

def modify(v,new):
    v.set_rental_price(new)
    print(f"Updated rental price for {v.brand} {v.model}: ${v.get_rental_price()}/day")
    
modify(car,100)