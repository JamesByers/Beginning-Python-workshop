
'''
Python for Data Science workshop
'''

'''
LISTS
'''

# creating
a = [1, 2, 3, 4, 5]     # create lists using brackets

# slicing
a[0]        # returns 1 (Python is zero indexed)
a[1:3]      # returns [2, 3] (inclusive of first index but exclusive of second)
a[-1]       # returns 5 (last element)

# appending
a[5] = 6        # error because you can't assign outside the existing range
a.append(6)     # list method that appends 6 to the end
a = a + [0]     # use plus sign to combine lists

# checking length
len(a)      # returns 7

# checking type
type(a)     # returns list
type(a[0])  # returns int

# sorting
sorted(a)               # sorts the list
sorted(a, reverse=True) # reverse=True is an 'optional argument'
sorted(a, True)         # error because optional arguments must be named




'''
EXERCISE:
1. Create a list of the first names of your family members.
2. Print the name of the last person in the list.
3. Print the length of the name of the first person in the list.
4. Change one of the names from their real name to their nickname.
5. Append a new person to the list.
6. Change the name of the new person to lowercase using the string method 'lower'.
7. Sort the list in reverse alphabetical order.
Bonus: Sort the list by the length of the names (shortest to longest).
'''



'''
TUPLES
'''
# (month number, month name, num days)
month = (1, 'January', 31)
month[1]


'''
DICTIONARIES
'''

# dictionaries are made of key-value pairs (like a real dictionary)
family = {'dad':'Homer', 'mom':'Marge', 'size':2}

# check the length
len(family)         # returns 3 (number of key-value pairs)

# use the key to look up a value (fast operation regardless of dictionary size)
family['dad']       # returns 'Homer'

# can't use a value to look up a key
family['Homer']     # error

# dictionaries are unordered
family[0]           # error

# add a new entry
family['cat'] = 'snowball'

# keys must be unique, so this edits an existing entry
family['cat'] = 'snowball ii'

# delete an entry
del family['cat']

# keys can be strings or numbers or tuples, values can be any type
family['kids'] = ['bart', 'lisa']   # value can be a list

# accessing a list element within a dictionary
family['kids'][0]   # returns 'bart'

# useful methods
family.keys()       # returns list: ['dad', 'kids', 'mom', 'size']
family.values()     # returns list: ['Homer', ['bart', 'lisa'], 'Marge', 2]
family.items()      # returns list of tuples:
                    # [('dad', 'Homer'), ('kids', ['bart', 'lisa']), ('mom', 'Marge'), ('size', 2)]


'''
EXERCISE:
1. Print the name of the mom.
2. Change the size to 5.
3. Add 'Maggie' to the list of kids.
4. Fix 'bart' and 'lisa' so that the first letter is capitalized.
Bonus: Do this last step using a list comprehension.
'''


#1. [your code here]

#2. [your code here]

#3. [your code here]

#4. [your code here]

# Bonus: [your code here]


