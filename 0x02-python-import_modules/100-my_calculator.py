#!/usr/bin/python3
if __name__ == "__main__":

    import calculator_1 as cal
    import sys

    def switch(operator):
        if operator == "+":
            return cal.add(a, b)
        elif operator == "-":
            return cal.sub(a, b)
        elif operator == "*":
            return cal.mul(a, b)
            # return a * b
        elif operator == "/":
            return cal.div(a, b)

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a, operator, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
        if operator in "+-*/":
            print("{} {} {} =".format(a, operator, b), switch(operator))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
