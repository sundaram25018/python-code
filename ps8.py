sum = 0
while(True):
    userInput = input("Enter the price : ")
    if(userInput!='q'):
        sum = sum + int(userInput)
    else:
        print("Thanks for using this calculator")
        print(f"Your total amount is {sum}")
        break