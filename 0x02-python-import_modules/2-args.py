#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n_args = len(sys.argv)
    txt = "argument" if n_args - 1 == 1 else "arguments"
    print("{} {}{}".format(n_args - 1, txt, "." if n_args - 1 == 0 else ":"))

    if (n_args - 1 > 0):
        for i in range(1, n_args):
            print("{}: {}".format(i, sys.argv[i]))
