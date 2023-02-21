from functools import reduce

list = ["a","b", "c"]

print("_".join(list))

########################################

alt = reduce(lambda x, y: x + "_" + y, list)
print(alt)