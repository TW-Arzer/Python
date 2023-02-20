
def multiplicateur(n):
	times = 1
	for i in n:
		times = i * times
	return lambda x: x * times
	
multi = multiplicateur([5, 3])

print(multi(4))
		
	