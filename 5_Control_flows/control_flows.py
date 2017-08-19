'''
If 
'''

if answer.lower() == 'yes':         # Line 1
    print("You are given gold.")    # Line 2
    player_gold = player_gold + 10  # Line 3
 
print("You put away your bag.")     # Line 4

'''
IF with ElSE
'''
if username.lower() == 'coder1':               # Line 1 
    print('Welcome back, Coder1!')             # Line 2
else:                                          # Line 3
    print('Your username is unrecognized.')    # Line 4

print('Thank you for using the system.')       # Line 5


'''
raw_input (interactive input)
'''
name = raw_input('What is your name? ')


'''
WHILE LOOP
'''

print('Type "yes" to continue.')                          # Line 1
# While the user does not enter 'yes', repeat!
while raw_input('> ') != 'yes':                           # Line 2
    print('Please type "yes" so we can exit this loop!')  # Line 3

print('Thank you for typing "yes".')                      # Line 4


# looping through a list using 'while'
primes = [2, 3, 5, 7]   	           # Line 1
i = 0                                  # Line 2
while i < len(primes):                 # Line 3
    print(primes[i])                   # Line 4
    i = i + 1                          # Line 5

print('Done!')                         # Line 6


# Using range to sum the first 100 integers
for num in range(101):
    total += num 


'''
FOR LOOPS AND LIST COMPREHENSIONS
'''

# for loop to print 1 through 5
nums = range(1, 6)      # create a list of 1 through 5
for num in nums:        # num 'becomes' each list element for one loop
    print num

# for loop to print 1, 3, 5
other = [1, 3, 5]       # create a different list
for x in other:         # name 'x' does not matter, not defined in advance
    print x             # this loop only executes 3 times (not 5)

# for loop to create a list of 2, 4, 6, 8, 10
doubled = []                # create empty list to store results
for num in nums:            # loop through nums (will execute 5 times)
    doubled.append(num*2)   # append the double of the current value of num

# equivalent list comprehension
doubled = [num*2 for num in nums]   # expression (num*2) goes first, brackets
                                    # Note we are storing results in a new list doubled
# Use range to sum the first 100 integers
for num in range(101):
    total += num 

'''
EXERCISE 1: Note: you may want to code a regular for loop first and then turn it into a list comprehension
Given that: letters = ['a', 'b', 'c']
Write a list comprehension that returns: ['A', 'B', 'C']
EXERCISE 2 (BONUS):
Given that: word = 'abc'
Write a list comprehension that returns: ['A', 'B', 'C']
EXERCISE 3 (BONUS):
Given that: fruits = ['Apple', 'Banana', 'Cherry']
Write a list comprehension that returns: ['A', 'B', 'C']
'''

letters = ['a', 'b', 'c']

word = 'abc'

fruits = ['Apple', 'Banana', 'Cherry']


