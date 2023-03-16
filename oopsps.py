class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def getdetail(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")
        print(f"salary : {self.salary}")
s = Employee("Sundaram", 20, 30000)
s.age = 19
s.getdetail()