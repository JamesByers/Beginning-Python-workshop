# This file contains solutions to the exercises in containers.py

'''
LIST:
EXERCISE
1. Create a list of the first names of your family members.
2. Print the name of the last person in the list.
3. Print the length of the name of the first person in the list.
4. Change one of the names from their real name to their nickname.
5. Append a new person to the list.
6. Change the name of the new person to lowercase using the string method 'lower'.
7. Sort the list in reverse alphabetical order.
Bonus: Sort the list by the length of the names (shortest to longest).
'''

family = ["August", "Diane", "Jade", "Janae"]
print family[-1]
print len(family[0])
family[0] = "Gus"
family.append("Kit Kat")
family[-1] = family[-1].lower
family.sort(reverse=True)
family.sort(lambda x,y: len(x) < len(y))


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



#1. Print the name of the mom.

print family['mom']

#2. Change the size to 5.

family['size'] = 5

#3. Add 'Maggie' to the list of kids.

family['kids'].append('Maggie')

#4. Fix 'bart' and 'lisa' so that the first letter is capitalized.
for kid in family['kids']:
    kid.capitalize()

#Bonus: Do this last step using a list comprehension.

family['kids'] = [kid.capitalize() for kid in family['kids']
