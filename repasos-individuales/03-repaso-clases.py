from abc import ABC, abstractmethod


class Department():
    def __init__(self, name: str, description: str, employees: list):
        self.name = name
        self.description = description
        self.__employees = employees

    def append(self, employee):
        self.__employees.append(employee)

    def get_employees(self):
        return self.__employees

    def get_number_employes(self):
        return len(self.__employees)

    def display_info(self):
        print(f"Department {self.name}")
        print(f"Department description: {self.description}")
        print(f"Number of employees {self.get_number_employes()}")
        for employee in self.get_employees():
            print(employee)


class Employee(ABC):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Nombre: {self.name} | type: {self.__class__.__name__}"

    @abstractmethod
    def calculate_pay(self, time):
        pass  # Each subclass will implement this differently

    @abstractmethod
    def display_info(self):
        pass

    def display_payment(self, time):
        print(f"Employee: {self.name} | Salary: ${self.calculate_pay(time)}")


class SalariedEmployee(Employee):
    def __init__(self, name, monthly_salary: float):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_pay(self, days: int):
        if days < 0:
            print("⚠ Days must be positive.")
            return 0
        price_per_day = self.monthly_salary / 30
        return price_per_day*days

    def display_info(self):
        print(
            f"Employee: {self.name} | monthly salary: ${self.monthly_salary}")


class HourlyEmployee(Employee):
    def __init__(self, name, hour_payment: float):
        super().__init__(name)
        self.hour_payment = hour_payment

    def calculate_pay(self, hours: int):
        if hours < 0:
            print("⚠ Hours must be positive.")
            return 0
        return self.hour_payment*hours

    def display_info(self):
        print(f"Employee: {self.name} | hour payment: ${self.hour_payment}")


if __name__ == "__main__":

    employee1 = SalariedEmployee("Laura", 1500)
    employee2 = HourlyEmployee("Fabian", 25)

    it_dept = Department("IT - Information Technology",
                         "The information Technology Department its responsible of all the technological systems", [employee1, employee2])
    it_dept.display_info()

    employee1.display_payment(30)
    employee2.display_payment(8)
