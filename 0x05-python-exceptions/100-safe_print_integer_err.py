#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        sys.stdout.write("{:d}".format(value))
        print()
        return True
    except Exception:
        sys.stderr.write("Unknown format code 'd' for object of type 'str'")
