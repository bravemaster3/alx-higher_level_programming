#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
    except Exception:
        result = None
    finally:
        if (result is None):
            print("Inside result: {}".format(None))
        else:
            print("Inside result: {:.1f}".format(result))
        return result