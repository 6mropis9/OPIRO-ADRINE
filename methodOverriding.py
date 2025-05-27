class Vehicle:
    def start_engine(self):
        print("Starting generic vehicle engine...")

class Car(Vehicle):
    def start_engine(self):
        print("Starting car engine with key or button...")

# Test
vehicle = Vehicle()
car = Car()

vehicle.start_engine()  # Output: Starting generic vehicle engine...
car.start_engine()      # Output: Starting car engine with key or button...cls
