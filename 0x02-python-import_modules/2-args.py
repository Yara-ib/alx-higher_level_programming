#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("{} argument.".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for arg in sys.argv:
            if count != 0:
                print("{}: {}".format(count, arg))
            count += 1
