from functools import reduce

villes = {"Zurich": 409241, "Genève": 200548, "Bale": 171513, "Lausanne": 138905, "Berne": 133798}

all = int(reduce(lambda x, y: x + y, villes.values()) / len(villes))

print(all)