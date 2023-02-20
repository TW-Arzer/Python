
def est_pair(a):
	check = lambda x: x % 2
	if check(a) == 0:
		print(True)
	else:
		print(False)
	
nomber = int(input("Please enter a number to check \n"))

est_pair(nomber)
	