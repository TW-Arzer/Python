
class Fraction:
	def __init__(self, num, denom):
		if denom == 0:
			raise ZeroDivisionError("Can't divide by zero")
		self.num = num
		self.denom = denom
		
	def __str__(self):
		return f"{self.num}/{self.denom} = {self.num/self.denom}"
						
if __name__ == "__main__":
	try:
		f1 = Fraction(1, 2)
		f2 = Fraction(64, 1024)
		f3 = Fraction(1, 2347)
	except ZeroDivisionError as e:
		print("Error: ", e)
	else:
		print(f1)
		print(f2)
		print(f3)
