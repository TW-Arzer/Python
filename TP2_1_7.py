import argparse
import math

parser = argparse.ArgumentParser(
    prog = "Logarithm",
    description = "Calculates the log of given argument")
parser.add_argument("-n", "--store", help = "Calculates the log, number must be positive")
args = parser.parse_args()

try:
    int_input = int(args.store)
    log = math.log(int_input)
except ValueError as e:
    print("This logarithm has the same mathematical rules as a normal log")
else:
    print(log)

