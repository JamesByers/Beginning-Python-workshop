# This file contains the solutions for the exercise in control__flows.py
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
[letter.upper() for letter in letters]  # iterate through a list of strings,
                                        # and each string has an 'upper' method
word = 'abc'
[letter.upper() for letter in word]     # iterate through each character

fruits = ['Apple', 'Banana', 'Cherry']
[fruit[0] for fruit in fruits]          # slice the first character from each string
