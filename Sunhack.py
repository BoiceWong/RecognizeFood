#// get Calories(string), instiatate them
#// pick 5 foods, average count calary
#// Sirloin steak - 280.8


fooditem = ""

path = "C:/Users/Boice Wong/Documents/SunHacks/TryTwo/tensorflow-for-poets-2/resultText.txt"
file = open(path, 'r')
fooditem = "" + file.read()  # this is

# method for converting the string of numbers into a list of numbers as strings


'''def string2list(string):
    string = string.strip()
    string = string[0:len(string) - 1].split(": ")
    return string


converted = string2list(string_numberset)
#'''
print("This is a " + fooditem)
# print(converted)  # ['0.9940024', '0.0059757535', '2.0527972e-05', '9.947543e-07', '3.1465524e-07']
