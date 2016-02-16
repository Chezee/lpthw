def cheese_and_crackers (cheese_count, cracker_boxes):
	print "You have %d cheeses!" % cheese_count
	print "You have %d crackers!" % cracker_boxes
	print "Man that's enough for party"
	print "Get a blanket.\n"

print "We can just give the function directly to function!"
cheese_and_crackers(20,30)

print "Or we can use variables from our script"
amount_of_cheese = 15
amount_of_crackers = 20
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside!"
cheese_and_crackers(5 + 7, 10 +3)

cheese_and_crackers(amount_of_cheese * 123, amount_of_crackers * 1.234)

