
l = ["John", "Ronald", "Reuel", "Tolkien"]

for i in range(1, len(l)-1):
	l[i] = l[i][0] + "." 
	
new = " ".join(l)

print(new)

	