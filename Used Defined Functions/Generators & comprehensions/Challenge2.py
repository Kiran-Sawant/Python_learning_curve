# Challenge 2: change the measures given in the tuple from inches to centimeters
#              using list comprehensions.
#              Them convert the code to return a tuple.

inch_measurement = (3, 8, 20)

cm_measure = tuple(x*2.54 for x in inch_measurement)
print(cm_measure)