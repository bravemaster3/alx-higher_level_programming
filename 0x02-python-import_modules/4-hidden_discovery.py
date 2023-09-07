#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    for i, var in enumerate(dir()):
        if var[0:2] != "__":
            print(var)
