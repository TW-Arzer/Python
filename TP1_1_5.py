
new_list = list(map(lambda x: x * 3, range(1,11)))

print(new_list)

####################################################

new_list2 = list(range(1,11))
calculated = []
for i in new_list2:
	i *= 3
	calculated.append(i)

print(calculated)