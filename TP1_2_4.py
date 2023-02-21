
def extraire_longs_mots(n):
	new = []
	l = n.split()
	for i in l:
		if len(i) > 3:
			new.append(i)
		else:
			pass
	new.sort()
	x = ",".join(new)
	return x
			
			
print(extraire_longs_mots("I like to move it"))