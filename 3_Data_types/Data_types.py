'''
Python data types
'''

'''
Multi-line comments go between 3 quotation marks.
You can use single or double quotes.
'''

# One-line comments are preceded by the pound symbol


# BASIC DATA TYPES

x = 5               # creates an object
x==5                # evaluates to True
print type(x)       # check the type: int (not declared explicitly)
type(x)             # automatically prints
type(5)             # assigning it to a variable is not required

type(5.0)           # float
type('five')        # str
type(True)          # bool

'''
STRINGS
'''

# creating
a = 'hello'     # can use single or double quotes

# slicing
a[0]        # returns 'h' (works like list slicing)
a[1:3]      # returns 'el'
a[-1]       # returns 'o'

# concatenating
a + ' there'        # use plus sign to combine strings
5 + ' there'        # error because they are different types
str(5) + ' there'   # cast 5 to a string in order for this to work

# uppercasing
a[0] = 'H'      # error because strings are immutable (can't overwrite characters)
a.upper()       # string method (this method doesn't exist for lists)

# checking length
len(a)      # returns 5 (number of characters)

dog = "Collie"
dog.upper()
dog
animal = dog
animal.upper()
