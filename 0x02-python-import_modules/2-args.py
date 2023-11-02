#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 1
    if len(sys.argv) > 1:
        print("{} arguments:".format(len(sys.argv) - 1))
    else:
        print("0 arguments.")
    for arg in sys.argv:
        if count != 1:
            print("{}: {}".format(count - 1, arg))
        count += 1
