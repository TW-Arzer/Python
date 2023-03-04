import argparse
from functools import reduce

parser = argparse.ArgumentParser(
    prog="Calculator",
    description="I guess it calculates")
parser.add_argument("-v", "--verbose", action="store_true") #not usable yet
parser.add_argument("-n", "--number", help="Enter more than 1 number, it's not that hard", required=True, nargs="+")
parser.add_argument("-o", "--operator", help="I can use +, -, *, /", choices=["+", "-", "*", "/"])
args = parser.parse_args()

if args.verbose:
    print("Mode verbose actif")
if len(args.number) > 0:
    print(f"{len(args.number)} entiers lus")

number_list = [int(x) for x in args.number]

if args.operator == "+":
    result_add = reduce(lambda x, y: x + y, number_list)
    print(result_add)
    with open("output.txt", "w+") as f:
        f.write(str(result_add))

elif args.operator == "*":
    result_mult = reduce(lambda x, y: x * y, number_list)
    print(result_mult)
    with open("output.txt", "w+") as f:
        f.write(str(result_mult))

elif args.operator == "-":
    result_sub = reduce(lambda x, y: x - y, number_list)
    print(result_sub)
    with open("output.txt", "w+") as f:
        f.write(str(result_sub))

elif args.operator == "/":
    result_div = reduce(lambda x, y: x / y, number_list)
    print(result_div)
    with open("output.txt", "w+") as f:
        f.write(str(result_div))

else:
    print("I don't even know what to do now")

f.close()