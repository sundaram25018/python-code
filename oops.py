# class Railway:
#     formType = "RailwayForm"
#     def printData(self):
#         print(f"Name is :",self.name)
#         print(f"Train is :",self.train)
# sandyApplication = Railway()
# sandyApplication.name = "Sundaram"
# sandyApplication.train = "Rajdhani Express"
# sandyApplication.printData()

class Employee:
    company = "Google"
    # salary = 100
    # @staticmethod
    # def greet():
    #     print("Hello good morning")
    def __init__(self,name,salary,unit):
        self.name = name
        self.salary = salary
        self.unit = unit
    def getdetail(self):
        print("name of employee : ", self.name)
        print("salary of employee : ", self.salary)
        print("unit of employee : ", self.unit)
        
harry = Employee("Sandy", 2000, "Morning")
harry.getdetail()

# sandy = Employee()
# harry.salary = 400
# sandy.salary = 500
# harry.greet()
# print(harry.company)
# print(sandy.company)
# Employee.company = "YouTube"
# print(harry.company)
# print(sandy.company)
# print(harry.salary)
# print(sandy.salary)