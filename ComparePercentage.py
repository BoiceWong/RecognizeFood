string_numberset = "0.9940024: 0.0059757535: 2.0527972e-05: 9.947543e-07: 3.1465524e-07: "

#method for converting the string of numbers into a list of numbers as strings
def string2list(string):
	string = string.strip()
	string = string[0:len(string) - 1].split(": ")
	return string


converted = string2list(string_numberset)
print converted #['0.9940024', '0.0059757535', '2.0527972e-05', '9.947543e-07', '3.1465524e-07']
print converted[0:2]

