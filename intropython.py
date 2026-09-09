print("Intro Python Stuff")
#Comment - does not execute - comments start with a #

#Python is case sensitive. Spaces don't matter in the code.
#String data type can use "" or ''

print("Hi")
print('Hi')

#print It's "groovy" day!
#causes problems due to quotes in quotes
#We can use escape sequence/characters to fix this and add behavior in a string
print("It's a \"groofy:\" day!")

#variables
#a name container that holds a value
#named container you can change the value in it
#use the assignment operator to put something in a variable
#variable names in python use "snake_case" convention

final_grade = 97
print("Your final grade:" + str(final_grade))

final_grade = 99
print("Your final grade:" + str(final_grade))

#Concatenate string see above

#formatting strings (f string)
name = "Rob"
print (f"Hello {name}! I see your final grade was {final_grade}.")