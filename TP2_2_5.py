import os

f = os.scandir(".")
list = []

for i in f:
    if i.is_file():
        list.append(i.name)

list.remove("TP2_2_5.py")
new = sorted(list)
j = 1

for i in new:
    os.rename(i, str(j) + ".txt")
    j += 1




