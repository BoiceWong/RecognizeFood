#// get Calories(string), instiatate them
#// pick 5 foods, average count calary

#// get Calories(string), instiatate them
#// pick 5 foods, average count calary
#// Sirloin steak - 280.8
#// mac n cheese - calories 219.0
#// Blue doritos - 150 calories
#// Gourmet Popcorn - 70 calories
#// Chewy peanut butter choco chip - 100 calories
#// make a list with a bunch of local variables
# string name = "Steak";
steak = 53.3  # per ounce
macNcheese = 376.0  # per cup
pizza = 258.0  # per slice
spaghetti = 463.0  # per bowl
chicken = 55.0  # per ounve
cal = 0.0

fooditem = ""

path = "C:/Users/Boice Wong/Documents/SunHacks/TryTwo/tensorflow-for-poets-2/resultText.txt"
file = open(path, 'r')
fooditem = "" + file.read()  # this is

# method for converting the string of numbers into a list of numbers as strings

if(fooditem == 'steak'):
    amount = raw_input("How many ounces of steak did you eat? ")
    cal = steak * amount
elif(fooditem == 'macandcheese'):
    amount = raw_input("How many bowls of Mac and Cheese did you eat? ")
    cal = macNcheese * amount
elif(fooditem == 'pizza'):
    amount = raw_input("How many slices of pizza did you eat? ")
    cal = pizza * amount
elif(fooditem == 'spaghetti'):
    amount = raw_input("How many plates of spaghetti did you eat? ")
    cal = spaghetti * amount
elif(fooditem == 'chicken'):
    amount = raw_input("How many ounces of chicken did you eat? ")
    cal = chicken * amount
else:
    amount = 0
    cal = 0


'''def string2list(string):
    string = string.strip()
    string = string[0:len(string) - 1].split(": ")
    return string


converted = string2list(string_numberset)
#'''
print("You ate " + fooditem)
print("You consumed " + str(cal) + " calories")
# print(converted)  # ['0.9940024', '0.0059757535', '2.0527972e-05', '9.947543e-07', '3.1465524e-07']
