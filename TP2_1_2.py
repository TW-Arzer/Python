import sys
from functools import reduce

list = sys.argv[1:]

if len(list) > 0:
	result = reduce(lambda x, y: x * y, list)
	print(result)
else:
	print(None)
	