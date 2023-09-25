#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
    except Exception:
        result = None
    finally:
        if (result != None):
            print("Inside result: {:.2f}".format(result))
        else:
            print("Inside result: {}".format(None))
        return result
