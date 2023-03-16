# a = {1,2,3, 4}
# print(type(a))
# print(a)
# # for empty set
# b = set()
# print(type(a))
# a.add(5)
# a.add(6)
# a.add(5)
# a.add((9,7,8))
# print(a)
# print(len(a))
# a.remove(5 )
# print(a)
# Union
# from ctypes import Union


# a = {1,3,5,6}
# b= {2,4,3,9}
# print(a.union(b))
# print(a.intersection(b))

## importing modules
import random
import math

## storing strings in a list
digits = [i for i in range(0, 10)]

## initializing a string
random_str = ""

## we can generate any lenght of string we want
for i in range(5):
## generating a random index
## if we multiply with 10 it will generate a number between 0 and 10 not including 10
## multiply the random.random() with length of your base list or str
  index = math.floor(random.random() * 10)

  random_str += str(digits[index])

## displaying the random string
print(random_str)