from functools import reduce

number = int(input("Fakultät der Nummer: "))
new_list = list(range(1, number + 1))

new = reduce(lambda x, y: x * y, new_list)

print(new)


