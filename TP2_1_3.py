import sys
from functools import reduce

list = sys.argv[1:]
int_list = []


for i in list:
    new_i = int(i)
    int_list.append(new_i)

try:
    result = reduce(lambda x, y: x / y, int_list)
except ZeroDivisionError as e:
    print("Division by 0 not defined")
except TypeError as e:
    print("None")
else:
    print(result)
