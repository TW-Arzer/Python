import sys

x = sys.argv[1:]
read_doc = []

try:
	for i in x:
		with open(i, "r") as open_doc:
			read_doc = open_doc.readlines()
except FileNotFoundError as e:
	print("Please check the path of your file")
else:
	new = " ".join(read_doc)
	print(new)
			
		
#####nonig fertig, muess zerst testet werde


