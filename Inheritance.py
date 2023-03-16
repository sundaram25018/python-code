# class Employee:
#     company = "Google"
#     def showDetail(self):
#         print("The detail about employee")
# class Programmer(Employee):
#     language = "Python"
#     def getlan(self):
#         print(f"The langauge is {self.language}")
# e = Employee()
# e.showDetail()
# p = Programmer()
# p.showDetail()
# p.getlan()

# class Employee:
#     company = "yahoo"
#     salary = 200
#     loccation = "Delhi"

#     @classmethod
#     def changedetail(cls, sal):
#         cls.salary = sal
# e = Employee()
# print(e.salary)
# e.changedetail(455)
# print(e.salary)

class Employee:
    salary = 5500
    bonus = 500

    @property
    def totalSalary(self):
        return self.salary+self.bonus

e = Employee()
print(e.totalSalary)
     