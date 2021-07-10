class Employee:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_nem = first_name
        self.last_name = last_name


    def set_salary(self, salary):
        self._salary = salary


a = Employee(1, "Robert", "Trzaska")
b= a.set_salary(120)
print(isinstance(b,))

