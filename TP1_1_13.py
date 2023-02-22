
def indent(word, space = "\t"):
	line = word.split("\n")
	indented_l = [space + i for i in line]
	indented_w = "\n".join(indented_l)
	return indented_w
	
print("zero\n" + indent("one\n" + indent("two\nthree", "\t-")))