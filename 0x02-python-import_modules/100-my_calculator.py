#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys

    n_args = len(sys.argv)
    if n_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ops = {
        "+": calc.add,
        "-": calc.sub,
        "*": calc.mul,
        "/": calc.div
    }
    if sys.argv[2] not in ops.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    res = ops[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3]))
    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], res))
