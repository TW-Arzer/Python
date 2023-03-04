import sys

r = sys.argv[1:]
for i in r:
    file_str = str(i)

try:
    f = open(file_str, "r")
except TypeError as e:
    print("Don't use <")
else:
    new = f.readlines()
    new1 = "".join(new)
    print(new1)

