numbers = []
def while_loop(i, y):
	while i < 6:
		print "At the top i is %d." % i
		numbers.append(i)
	
		i = i + y
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
x = int(raw_input("Print number: "))
z = int(raw_input("Print increment:" ))
while_loop(x, z)

print "Numbers: "

for num in numbers:
	print num 