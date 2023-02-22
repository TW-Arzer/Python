
l = [[2, 3, 4], [1], [2, 7]]

x = "/".join(["".join(map(str, new)) for new in l])
print(x)
