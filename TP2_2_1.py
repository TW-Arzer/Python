import argparse

parser = argparse.ArgumentParser(
    prog = "Puissance",
    description = "Calculates the puissance (--e) of --n")
parser.add_argument("-n", "--store", help="Figure it out yourself stupid", type=int)
parser.add_argument("-e", "--puissance", help="It's pretty obvious isn't it?", default=1, type=int)
args = parser.parse_args()

result = args.store ** args.puissance
print(result)