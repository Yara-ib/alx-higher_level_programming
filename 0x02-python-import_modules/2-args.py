#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    if len(sys.argv) > 1:
        print("{} arguments:".format(len(sys.argv) - 1))
    else:
        print("0 arguments.")
    for arg in sys.argv:
        if count != 0:
            print("{}: {}".format(count, arg))
        count += 1
