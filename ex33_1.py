numbers = []
def while_loop(x, y, z):
	for i in range(x, y, z):
		print "At the top i is %d." % i
		numbers.append(i)
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

a = int(raw_input("Print start: "))
b = int(raw_input("Print range: "))
c = int(raw_input("Print increment:" ))
while_loop(a, b ,c)