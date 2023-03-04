import argparse

parser = argparse.ArgumentParser(
    prog = "Quadrieren",
    description = "Calculates **2 of --n")
parser.add_argument("-n", "--entier", help="Figure it out yourself stupid", type=int, required=True)
parser.add_argument("-o", "--output", help="Writes Values in a .txt file (True or False)", default=False, type=bool)
args = parser.parse_args()

result = args.entier**2
print(result)

while args.output == True:
    f = open("resultat.txt", "w+") ## w+ generiert eine Datei mit dem Namen, falls keine existiert, w alleine braucht Datei
    f.write(str(result))
    f.close()
    args.output = False


