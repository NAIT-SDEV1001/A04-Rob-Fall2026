#list is a collection of values
#each value is stored in an element
#can hold different datatypes (including other list)

#create a list using []
colors = ['red', 'blue', 'green', 'yellow']

#display the list
print(colors)

#get a specific item at an element by using index
#index is zero based - meaining it starts at 0
print(colors[2])

#change a item at an element using index
colors[3] = 'white'
print(colors)

#slicing
#gets values from a range in the list
letters = ["a","b","c","d","e"]
print(f"First three letters: {letters[0:3]}")
#with slicing the upper boundary is not inclusive

#if you start at the first index it can be omitted
print(f"First three letters: {letters[:3]}")

#if you start at the end you can omit as well
print(f"Last 2 letters: {letters[-2:]}")
