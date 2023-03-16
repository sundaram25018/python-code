# def percent(marks):
#     return (sum(marks)/500)*100

# m1 = [78,98,45,75,65]    
# m1 = percent(m1)
# print(m1)

# from itertools import product


# def Print(n):
#     product = 1
#     for i in range(n):
#       product = product*(i+1)
#     print(product)

# n1 = int(input("Enter your number"))
# Print(n1)



# def greeting(name):
#     print("Good morning", name)

# a = input("Enter your name ")    
# greeting(a)

# print("HII", end=" ")
# print("Hello", end=" ")
# print("Vadakkam", end=" ")

# s = int(input("enter the upper value"))
# e = int(input("enter the lower value"))
# print ("The Prime Numbers in the range are: ")  
# for number in range (s, e):  
#     if number > 1:  
#         for i in range (2, number):  
#             if (number % i) == 0:  
#                 break  
#         else:  
#             print (number) 
def isprime(n):
    for i in range(2, n):
      if((n%i)==0):
       return True
    else:
      return False
n = int(input("enter the number"))
if(isprime(n)):
  print("the number is not prime")
else:
  print("the number is prime")