def add(a, b):
	print "Adding %d and %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "Subtracting %d and %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "Multiplying %d and %d" % (a, b)
	return a * b
	
def divide(a,b):
	print "Dividing %d and %d" % (a, b)
	return a / b
	
age = add(30, 5)
height = subtract(30, 24)
weight = multiply(2, 84)
iq = divide (225, 5)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here's a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "Here becomes: ", what, "Can you do it by hand?"

puzzle = subtract(float(add(24, float(divide(34, 100)))), 1023)

print "Another 1 puzzle: ", puzzle