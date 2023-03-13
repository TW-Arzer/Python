import math

class Fraction:
	
	def __init__(self, num=0, denom=1):
		self.__num = int(num)
		self.__denom = int(denom)
		
	def __str__(self):
		return f"{self.__num}/{self.__denom}"
		
	def __eq__(self, other):
		if self.__num * other.__denom == self.__denom * other.__num:
			return f"Is {self.__num}/{self.__denom} equal to {other.__num}/{other.__denom}? True"
		else:
			return f"Is {self.__num}/{self.__denom} equal to {other.__num}/{other.__denom}? False"
			
	def get_num(self):
			return self.__num
			
	def set_num(self, num):
			self.__num = num
			
	def get_denom(self):
			return self.__denom
			
	def set_denom(self, denom):
			self.__denom = denom
				
	def integer(self):
		y = self.__num/self.__denom
		x = y.is_integer()
		if x == False:
			return False
		else:
			raise TypeError(f"{self.__num}/{self.__denom} is {y} - not a Fraction")
			
	def value(self):
			return self.__num / self.__denom
			

if __name__ == "__main__":
	f1 = Fraction(5, 2)
	f2 = Fraction(10, 4)
	test = f1.integer()
	
	print(f1)