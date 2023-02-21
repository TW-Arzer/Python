
def lister_int(n):
	list = [n]
	while n > 1:
		list.insert(0, n-1)
		n -= 1
	return list

new = ",".join(map(str, lister_int(10)))

print(new)

		