
new_list = list(map(lambda x: x * 3, filter(lambda x: x % 2 == 0, range(1, 11))))

print(new_list)

################################################

new_list2 = list(range(1, 11))
calculated = [3*i for i in new_list2 if i % 2 == 0]
	
print(calculated)