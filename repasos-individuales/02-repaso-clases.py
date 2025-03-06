"""
    Employee Management System
    """


class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.__salary = salary  # Private attribute (encapsulation)

    def display_info(self):
        print(f"Employee: {self.name} | Salary: ${self.__salary}")

    def increase_salary(self, percentage: float):
        if percentage > 0:
            self.__salary += self.__salary * (percentage/100)
            print(f"✅ {self.name}'s salary increased by {percentage}%")
        else:
            print("⚠ Percentage must be positive.")

    def get_salary(self):  # The getter method to access private salary
        return self.__salary


class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print(
            f"Manager of {self.department}: {self.name} | Salary: ${self.get_salary()}")


if __name__ == "__main__":
    employee1 = Employee("Laura", 9999)
    employee2 = Employee("Fabian", 1500)

    employee1.display_info()
    print(f"employee1 salary ${employee1.get_salary()}")
    employee1.increase_salary(0)
    employee1.increase_salary(25.2)
    employee1.display_info()

    manager1 = Manager("Sebastian", 2500, "Ventas")
    manager1.display_info()
    manager1.increase_salary(10)
    manager1.display_info()
