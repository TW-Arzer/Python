import sys
from functools import reduce

list = sys.argv[1:]
int_list = []


if len(list) > 0:
	for i in list:
		new_i = int(i)
		int_list.append(new_i)
	result = reduce(lambda x, y: x * y, int_list)
	print(result)
else:
	print(None)
	
