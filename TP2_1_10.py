import sys

list = sys.argv[1:]
for i in list:
    f = str(i)

try:
    f1 = open(f, "r")
except TypeError as e:
    print("Couldn't open file, check name and location and try again")
else:
    new = f1.readlines()
    for j in new:
        splited = j.split(", ")
        dict = {splited[j]:splited[j + 1] for j in range(0, len(splited), 2)}
        print(dict)