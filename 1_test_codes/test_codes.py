ex_1 = False
ex_2 = 29
ex_3 = 4.1352

print(type(ex_1))
print(type(ex_2))
print(type(ex_3))

ex_4 = str(False)
ex_5 = str(29)
ex_6 = str(4.1352)

print(type(ex_4))
print(type(ex_5))
print(type(ex_6))


#######
import numpy as np

intVal = 5

floatVal = 2.21

boolVal = False

print(boolVal)

boolVal = True

print(intVal)

print(floatVal)

print(boolVal)

l = [1, 2]
nplist = np.array(l)
print(nplist)

################################
diego = 'diego likes the gym.'
print(diego[3:8])
###
print("cars"[0])
###
concatenated = "R2" + "-" + "D2"
print(concatenated)
print(concatenated[3])
print(concatenated[1:4])
###
unchanged = "forest gump"
sliced = unchanged[:6]
print(sliced)
print(unchanged)
print(unchanged[10])
print(unchanged)

#############

# The \t gives a extra space between the words.

print("My\tcar\tis\ttoo\tbig")

# The \n divides the phase.
print("My\ncar\nis\ntoo\nbig")

# The \" add quotes to the phase.

print("\"Mycar is too big\"")

# The double back-slash(\\) can be used for adding slash in any part o the phase.

print("Mycar is too big\\.")

# Exercise.

print("*******\n ***** \n  ***  \n   *  ")

#name = input("Please enter your name.")
#print("Your name is " + name + ".")
#print(type(name))

#fav_num = input("Please enter your favorite number?")
#print("Your favorite number is " + fav_num + ".")
#print(type(fav_num))

#guest = input("Please enter your guest name?")
#print("Your guest name is " + guest + ".")
#print(type(guest))

#print(("Your guest name is " + guest + "."), ("Your favorite number is " + fav_num + "."), ("Your name is " + name + "."))

#How will you verify if the items present in list A are present in series B? We will use the isin() function. For this, we create two series s1 and s2 –

import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([4, 5, 6, 7, 8])
s3 = s1[s1.isin(s2)]
print(s3)

#How to find the positions of numbers that are multiples of 4 from a series? For finding the multples of 4, we will use the argwhere() function. First, we will create a list of 10 numbers –

#s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#np.argwhere(ser % 4==0)

#Can you stack two series horizontally? If so, how?Yes, we can stack the two series horizontally using concat() function and setting axis = 1.
df = pd.concat([s1, s2], axis=1)
print(df)

#How can you convert date-strings to timeseries in a series?
#Input:

s = pd.Series(['02 Feb 2011', '02-02-2013', '20160104', '2011/01/04', '2014-12-05', '2010-06-06T12:05'])

#To solve this, we will use the to_datetime() function.

print(pd.to_datetime(s))

user_int = int(input("Please enter an integer."))
print(user_int)
print(type(user_int))


user_float = float(input("Please enter the float."))
print(user_float)
print((type(user_float)))



