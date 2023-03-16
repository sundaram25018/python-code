from locale import currency


with open('data.txt') as f:
    lines = f.readlines()
currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]
   
amount = int(input("Enter your amount"))
print("Enter your currency: \n")
[print(item) for item in currencyDict.keys()]
currency = input("Enter one of these value: \n")
print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")