import sys
from functools import reduce

list = sys.argv[1:]
int_list = []


for i in list:
	new_i = int(i)
	int_list.append(new_i)
	if int_list[1] == 0:
		raise ZeroDivisionError("Can't divide by 0")
	if len(list) > 0:		
		result = reduce(lambda x, y: x / y, int_list)
		print(result)
	else:
		print(None)
	
