
class Individu:
	def __init__(self, prenom, nom, age=0):
		self.__prenom = prenom
		self.__nom = nom
		self.__age = age
		
	def __str__(self):
		if self.__age != 0:
			return f"{self.__prenom} ({self.__age} ans)"
		else:
			return f"{self.__prenom} {self.__nom} est né"
			
	def get_prenom(self):
		return self.__prenom
		
	def set_prenom(self, prenom):
		self.__prenom = str(prenom)

	def get_nom(self):
		return self.__nom
		
	def set_nom(self, nom):
		self.__nom = str(nom)
		
	def get_age(self):
		return self.__age
	
	def set_age(self, age):
		self.__age = int(age)		
		
		
if __name__ == "__main__":
		person1 = Individu("Yannic", "Lüthi", 0)
		
		print(person1)
