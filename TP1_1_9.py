
def check(x):
	if x % 2 == 0:
		return True
	else:
		return False

d = {i: check(i) for i in [1,2,3,4]}
	
print(d)
