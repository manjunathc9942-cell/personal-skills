# -------------------------------------------------------------------------
# 1. THE PARENT CLASS (Base Class)
# -------------------------------------------------------------------------
class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"Car Name: {self.name}")
        print(f"Price: ${self.price:,}")


# -------------------------------------------------------------------------
# 2. THE FIRST CHILD CLASS (Electric Variant)
# -------------------------------------------------------------------------
class ElectricCar(Car):
    def __init__(self, name, price, battery_capacity):
        super().__init__(name, price) # Inherits name and price
        self.battery_capacity = battery_capacity

    def show(self):
        super().show()
        print(f"Battery Capacity: {self.battery_capacity} kWh")


# -------------------------------------------------------------------------
# 3. THE SECOND CHILD CLASS (Hybrid Variant)
# -------------------------------------------------------------------------
class HybridCar(Car):
    def __init__(self, name, price, fuel_efficiency):
        # Calls the Parent class constructor to initialize 'name' and 'price'
        super().__init__(name, price) 
        
        # Unique attribute only relevant to Hybrid cars
        self.fuel_efficiency = fuel_efficiency

    # Overriding the parent method to include hybrid specifications
    def show(self):
        super().show()
        print(f"Fuel Efficiency: {self.fuel_efficiency} MPG")


# -------------------------------------------------------------------------
# EXECUTION AND VERIFICATION
# -------------------------------------------------------------------------
print("--- 1. Instantiating Parent Class ---")
regular_car = Car("Benz", 200000)
regular_car.show()

print("\n--- 2. Instantiating First Child Class ---")
ev_car = ElectricCar("Tesla Model S", 90000, 100)
ev_car.show()

print("\n--- 3. Instantiating Second Child Class ---")
# HybridCar automatically gets name, price, and extends the show() method!
hybrid_car = HybridCar("Toyota Prius", 35000, 54)
hybrid_car.show()