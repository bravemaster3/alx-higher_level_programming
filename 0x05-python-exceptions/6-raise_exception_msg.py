#!/usr/bin/python3
def raise_exception_msg(message=""):
    class custom_except(Exception):
        print(message)
