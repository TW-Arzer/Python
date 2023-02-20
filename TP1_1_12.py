
l = [7, 1, 4, 0]
v = int(input("Number to check: "))


def plus_petit_des_plus_grands(a, b):
	x = sorted(a)
	for i in x:
		if i - b > 0:
			return i
		
			
print(plus_petit_des_plus_grands(l, v))