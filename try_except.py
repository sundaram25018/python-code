# print("Enter number 1")
# n1 = int(input())
# print("Enter number 2")
# n2 = input()
# try:
#     print(n1+n2)
# except Exception as e:
#     print(e)

# print("this line is very important")

# while(True):
#     print("Press q to quit")
#     a = input("Enter your number : ")
#     if(a=='q'):
#         break
#     try:
#         a= int(a)
#         if(a>8):
#             print("you enter number greater than 8")
#     except Exception as e:
#         print(e)
# print("Thank you for doing this")

def increament(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Harry")
a = increament('ndnnd')
print(a)
