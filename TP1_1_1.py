
def function(n):
	return lambda a: a * n
	
triple = function(3)
nomber = int(input("Nomber to be multiplied: \n"))

print(triple(nomber))
	
