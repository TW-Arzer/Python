import sys
from functools import reduce

list = sys.argv[1:]

list1 = [i for j in list for i in j]

if list1[-1] == "+":
    list1.remove("+")
    list_add = [int(x) for x in list1]
    result_add = reduce(lambda x, y: x + y, list_add)
    print(result_add)

elif list1[-1] == "*":
    list1.remove("*")
    list_mult = [int(x) for x in list1]
    result_mult = reduce(lambda x, y: x * y, list_mult)
    print(result_mult)

elif list1[-1] == "-":
    list1.remove("-")
    list_sub = [int(x) for x in list1]
    result_sub = reduce(lambda x, y: x - y, list_sub)
    print(result_sub)

elif list1[-1] == "/":
    list1.remove("/")
    list_div = [int(x) for x in list1]
    result_div = reduce(lambda x, y: x / y, list_div)
    print(result_div)

else:
    print("I don't even know what to do now")