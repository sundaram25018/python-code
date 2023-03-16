t1 = (3,5,7,9.3,4,3)
# cannot we updata tuples
print(t1)
t1.count(7)
# dict = {
#   "calculator": 1,
#   "Money" : 5
# }
# print(dict['calculator']+1)
# print(dict.get)

name = {
    1: "Sundaram",
    2: "Dubey"
}
print(name.get(1))
print(name.keys())
updatedic = {
    3: "Manoj"
}
name.update(updatedic)
print(name.keys())
print(name)