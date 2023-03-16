# class Programmer:
#     company = "Microsoft"
#     def __init__(self,name,product):
#         self.name = name
#         self.product = product
    
#     def getinfo(self):
#         print(f"The name of programmer is {self.name}")
#         print(f"Working on {self.product}")

# harry = Programmer("Sandy","Skype")
# sandy = Programmer("Sundaram", "Phone")
# harry.getinfo()
# sandy.getinfo()
class calculator:
    def __init__(self, num):
           self.num = num

    def square(self):
        print(f"The value of {self.num} square is {self.num **2}")

    def squareRoot(self):
        print(f"The value of {self.num} squareRoot is {self.num **0.5}")
    def cube(self):
        print(f"The value of {self.num} cube is {self.num **3}")
    
cal = calculator(25)
cal.square()
cal.squareRoot()
cal.cube()

        

        