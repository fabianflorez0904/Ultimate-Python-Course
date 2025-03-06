class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0  # New attribute
        self.fuel_level = 100
        self.fuel_consume_per_km = 1  # 1%/km

    def display_info(self):
        print(f"Car: {self.year} {self.brand} {self.model}")
        print(f"Mileage: {self.mileage} km")
        print(f"fuel_level: {self.fuel_level}%")
        print(f"fuel_duration: {self.calculate_fuel_duration()}km")

    def calculate_fuel_duration(self):
        return round(self.fuel_level/self.fuel_consume_per_km)

    def start_engine(self):
        if self.fuel_level == 0:
            print("⛔ The engine can't start because it's no fuel.")
        else:
            print("🚗 The engine is now running.")

    def stop_engine(self):
        print("⛔ The engine is now off.")
        if self.fuel_level == 0:
            print("⛔ The fuel level is 0, you have to refuel")

    def drive(self, km: int):
        if km > 0 and km <= self.calculate_fuel_duration():
            self.mileage += km
            self.fuel_level -= self.fuel_consume_per_km * km
            print(
                f"🚙 You drove {km} km. Total mileage: {self.mileage} km. Your fuel level is {self.fuel_level}%")
        elif km > self.calculate_fuel_duration():
            km_recorridos = self.calculate_fuel_duration()
            self.mileage += km_recorridos
            self.fuel_level -= self.fuel_consume_per_km * km_recorridos
            print(
                f"🚙 You drove {km_recorridos} km. Total mileage: {self.mileage} km. Your fuel level is {self.fuel_level}%")
            self.stop_engine()
        else:
            print("⚠ Distance must be positive.")

    def refuel(self, amount):
        if amount > 0:
            fuel_remaning = 100 - self.fuel_level
            if amount < fuel_remaning:
                self.fuel_level += amount
                print(
                    f"The fuel level is enough for: {self.calculate_fuel_duration()}kms")
            else:
                self.fuel_level = 100
                print(f"The fuel level is now full: {self.fuel_level}%")


# Creating an object
my_car = Car("Toyota", "TXL", 2022)

# Using the methods
my_car.display_info()
my_car.start_engine()
my_car.drive(80)  # Driving 100 km
my_car.display_info()
my_car.drive(40)
my_car.refuel(99)
my_car.display_info()
my_car.start_engine()
my_car.drive(99)
my_car.drive(1)
my_car.display_info()
