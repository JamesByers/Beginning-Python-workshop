

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
                                    # indicate we are storing results in a list


'''
EXERCISE 1:
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
[letter.upper() for letter in letters]  # iterate through a list of strings,
                                        # and each string has an 'upper' method
word = 'abc'
[letter.upper() for letter in word]     # iterate through each character

fruits = ['Apple', 'Banana', 'Cherry']
[fruit[0] for fruit in fruits]          # slice the first character from each string

