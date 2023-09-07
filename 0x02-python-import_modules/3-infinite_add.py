#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    n_args = len(sys.argv)
    if (n_args - 1 > 0):
        for i in range(1, n_args):
            sum += int(sys.argv[i])
    print(sum)
