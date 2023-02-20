from functools import reduce

def produit(a, b):
	return lambda a, b: a * b
	
new_list = list(range(1, 11))

new = reduce(produit(new_list, new_list), new_list)

print(new)
