#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
print("My first name is {}".format(lc.first_name))
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

lc1 = LockedClass("Paul")
print("My first name is {}".format(lc1.first_name))

lc3 = LockedClass()
print("My first name is {}".format(lc1.first_name))
