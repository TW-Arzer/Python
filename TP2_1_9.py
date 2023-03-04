import argparse

file = open("cambriolage.txt", "w+")


parser = argparse.ArgumentParser(
    prog = "Cambriolages",
    description = "Affiches toutes cambriolages")
parser.add_argument("-n", "--date", help="Date", required=True)
parser.add_argument("-i", "--place", help="Place", required=True)
parser.add_argument("-s", "--price", help="Costs", required=True)
args = parser.parse_args()

file.write(f"Un cambriolage a eu lieu le {args.date} à {args.place}. Le montant estimé est de {args.price} CHF\n")
print(f"Un cambriolage a eu lieu le {args.date} à {args.place}. Le montant estimé est de {args.price} CHF")
file.close()