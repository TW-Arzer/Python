import argparse

parser = argparse.ArgumentParser(
    prog = "Stupid",
    description = "Does something, no idea what and why")
parser.add_argument("-i", "--entier", help = "Un entier positif", type = int)
parser.add_argument("-s", "--chaine", help = "Un chaine de caracteres")
args = parser.parse_args()

print(f"s = {args.chaine}")
print(f"i = {args.entier}")