from turtle import update


myDict = {
    "Fast" : "In a quick Manner",
    "Sandy" : "A softwere developer",
    "marks" : [1,3,5],
    "anotherDict": {'Man': 'Player'}
}
print(myDict['Fast'])
print(myDict['Sandy'])
print(myDict['marks'])
print(type(myDict))
print((myDict.values()))
print((myDict.items()))
print(list(myDict.keys()))
print(myDict['anotherDict']['Man'])
print(myDict)
updateDict = {
    "Aman" : "A cricket player"
}
myDict.update(updateDict)
print(myDict)
print(myDict.get["Sandy"])
