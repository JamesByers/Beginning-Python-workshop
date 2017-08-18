###### Python for data science
# Control Flow

----------------------------------

## By the end of this section you will be able to:

+ Create `if`/`else` statements.
+ Create `while` statements.
+ Create `for` loops.

<!--
----------------------------------

## Expressions

#### An **expression** is any valid piece of code that evaluates to something. Notice that we can convert any expression to a particular data type

For example, let's convert some expressions to booleans using the built-in function `bool()`:

```
bool(1 + 1) -> True      # Any non-zero integer is True
bool(0) -> False

bool('Hi' + ' there') -> True   # Any non-empty string is True
bool('') -> False
```

> Experiment with other data types! Can you guess what evaluates to `True`/`False` for `dict`s, `set`s, and `tuple`s?
-->
----------------------------------

## The `if` Statement

#### Here is an example of using `if`: 

```
if answer.lower() == 'yes':         # Line 1
    print("You are given gold.")    # Line 2
    player_gold = player_gold + 10  # Line 3
 
print("You put away your bag.")     # Line 4
```

- This code is evaluated line by line, top to bottom. Note that lines 1-3 are all part of the same `if` code block
- Line 4 comes after the if code block.

Starting on Line 1, we evaluate the expression `answer.lower() == 'yes'`:

+ If the "expression answer.lower() == 'yes'"evaluates to `True` then the indented lines 2 and 3 are evaluated. 
+ Next, after the `if` block is completed, Line 4 is evaluated.
+ If the expression is `False`, we skip the `if` block and only evaluate Line 4. (It is the next line on the same level as Line 1.)

----------------------------------

## The `if` Statement, Cont.

The `if` statement has a very particular structure. Every `if` statement *must*:

- Begin the line with `if`, followed by
- any expression, followed by
- a colon, followed by
- one or more indented lines of code.

```
if <expression>:
	<indented line of code>
	...
```

- We evaluate the indented lines of code only if the expression (converted to a bool) is `True`
- You can think of this as "If the expression is True, then evaluate the indented code."

> **Pro tip:** According to [PEP 8](https://www.python.org/dev/peps/pep-0008/), lines should be indented using **four spaces**.
<!--
----------------------------------

> Knowledge Check | Multiple Choice;

_description_ Select the best answer.

_Prompt*_: What are the values of `num_answers` and `answer` after evaluating the following code?

```
answer = 'yes'
num_answers = 0

if answer:
    num_answers = num_answers + 1

answer = ''
```

_Choices:*_

1. `num_answers = 0` and `answer = 'yes'`
2. `num_answers = 1` and `answer = 'yes'`
3. `num_answers = 0` and `answer = ''`
4. `num_answers = 1` and `answer = ''` *

_Explanation*_: Recall that we evaluate the lines one by one, top to bottom. So, we immediately evaluate `answer = 'yes'` followed by `num_answers = 0`.

Now, recall that any non-empty string converted to a boolean is `True`. So, the `if` statement is checking whether `answer` is a non-empty string. If it is non-empty, it increments `num_answers` by one. In this case, `answer` is non-empty, so `num_answers` is set to `1`.

Finally, the final line is evaluated, since it is at the same indentation level as the `if` statement. So, `answer = ''` and `num_answers = 1`.
-->
----------------------------------

## The `else` Condition

##### Sometimes, we want to evaluate one block of code if the expression is `True`, and another block of code if it is `False`. For example:

```
if username.lower() == 'coder1':               # Line 1 
    print('Welcome back, Coder1!')             # Line 2
else:                                          # Line 3
    print('Your username is unrecognized.')    # Line 4

print('Thank you for using the system.')       # Line 5
```

- In the code we display a different message based on if the username is `'coder1'`.

- If the expression `username.lower() == 'coder1'` is `True`, then the first set of indented lines are evaluated (Line 2). If it is `False`, then the second set of indented lines are evaluated (Line 4).

- In either case, Line 5 is at the same indentation level as Line 1. So, it is evaluated immediately after the `if` block.
<!--
----------------------------------

> Knowledge Check | Multiple Choice

_Descritpion_: Select the best answer.

_Prompt*_: How could we condense the following `if` statement?

```
if test_number in prime_numbers:
    is_prime = True
else:
    is_prime = False
```

_Choices:*_

1. `is_prime = (test_number in prime_numbers)` *
2. `is_prime = bool(test_number)`
3. `is_prime = True`
4. `is_prime = prime_numbers.contains(test_number)`

_Explanation*_: Because the expression `test_number in prime_numbers` itself evaluates to `True` or `False`, we can just set `is_prime` to it. Interestingly, the `in` operator is how you test for membership in containers. There is no `contains` method, as you may expect!

----------------------------------

_Slide Title:_ Learning Objective

_Slide Content:_

**Create `while` statements.**

In this section, we will look at our first loop — `while` statements.
-->
----------------------------------

## Playing With User Input: `raw_input`

#### A fun built-in Python function is `raw_input`
- This function prompts the user for text input. Then, it returns the user's input as a string

For example:

```
name = raw_input('What is your name? ')
```

- In the code the user is prompted `What is your name? `
- If the user enters `Melissa`, then `name` is set to the string `"Melissa"`.

- Here is a helpful way of reading code with function calls: Replace the entire function call (in this case, `raw_input('What is your name? ')`) with its return value. Thinking about it this way, the statement becomes `name = "Melissa"`.

> **Pro tip:** In Python 3, the `raw_input` built-in function was renamed to `input`.

----------------------------------

## The `while` Statement

#### Here is an example:

```
print('Type "yes" to continue.')                          # Line 1

# While the user does not enter 'yes', repeat!
while raw_input('> ') != 'yes':                           # Line 2
    print('Please type "yes" so we can exit this loop!')  # Line 3

print('Thank you for typing "yes".')                      # Line 4
```

Let's evaluate the code line by line from top to bottom. Line 1 is evaluated, then we move to Line 2 — the `while` statement. 

You can think about the `while` statement as a repeated `if` statement. Just as with `if`, we must first evaluate the expression `raw_input('> ') != 'yes'`:

- If `True`, we evaluate the indented code. Afterward, we loop back to Line 2 and re-evaluate it.
- If `False`, we jump to the line after the indented code, Line 4.

> Let's walk through `raw_input('> ') != 'yes'`. To do the comparison, we must first evaluate `raw_input('> ')`. So, the user is prompted with `'> '`. Suppose the user enters `'no'`. Then, replacing the function call in its entirety with `'no'`, we get: `'no' != 'yes'`. This is `True`, since `'no'` is not equal to `'yes'`.

----------------------------------

## The `while` Statement, Cont.

A `while` loop is generally used in Python when it is not known when the looping will stop. Or, when we do not know how many iterations the loop will require. For example, it is unknown when the user will enter `'yes'` in the last example. So, using a `while` loop here is appropriate.

The `while` loop is in many ways the most basic looping construct. All other loops can be rewritten as a `while` loop.

----------------------------------
<!--

> Knowledge Check | Multiple Select

_Description_: Select all that apply.

_Prompt*_: Which of the following would be a good use of the `while` loop, where we do not know the number of iterations in advance?

_Choices:*_

1. Loop while less than 33 milliseconds have elapsed, then continue. *
2. Loop while we have not received the entire downloaded file. *
3. Loop until a new random number between 0 to 1 is greater than 0.9. *
4. Loop through each element of a Python list.

_Explanation*_: Python lists have a finite size, which we know in advance! (We will cover looping through them using the `for` loop in the next section.) In video games, a `while` loop is often used to wait until 33 milliseconds have elapsed — this guarantees an exact 30 frames per second. We do not know the number of iterations in advance here because execution speed can vary even on a single processor, muchless between computers.

----------------------------------
-->

## Looping Through a List Using `while`

#### Let's take a look at how we might print each element of a list using a `while` loop

Generally, in Python this is done using a `for` loop (we'll see this next!). However, it is a good exercise to get insight into how Python's `for` loop might work.

```
primes = [2, 3, 5, 7]   	       # Line 1

i = 0                                  # Line 2
while i < len(primes):                 # Line 3
    print(primes[i])                   # Line 4
    i = i + 1                          # Line 5

print('Done!')                         # Line 6
```

Here, we are using the variable `i` as an index into the `primes` list.

First, lines 1 and 2 are evaluated. Note that lines 3-5 are the `while` code block. Once the `while` loop is finished, we will evaluate Line 6.

> When you use `i` as a variable name, it must always refer to an index. This is one of the few times you can use a short variable name, since it is so universally understood.

----------------------------------

## Looping Through a List Using `while`, Cont.

```
primes = [2, 3, 5, 7]                  # Line 1

i = 0                                  # Line 2
while i < len(primes):                 # Line 3
    print(primes[i])                   # Line 4
    i = i + 1                          # Line 5

print('Done!')                         # Line 6
```

- The Python interpreter first evaluates Line 3. Is `i < len(primes)`? Well, `i` is `0` and `len(primes)` is 4. So, `i < len(primes)` becomes `0 < 4`, which is `True`. Hence, we execute Line 4 — the value of `primes[0]` is displayed (`2`). Now Line 5 is evaluated and `i` is incremented to `1`.

- Then it evaluates Line 3 again. Is `i < len(primes)`? Now, `i` is `1` and `len(primes)` is still 4. So, `i < len(primes)` becomes `1 < 4`, which is `True`. Hence, we execute Line 4 — the value of `primes[1]` is displayed (`3`). Now, Line 5 is evaluated and `i` is incremented to `2`.

- This is continued until finally `i` is 4. At this point, `i < len(primes)` is evaluated to `4 < 4` which is `False`. So, we jump to the line after the code block, Line 6, and display `Done!`.

----------------------------------
<!--

> Knowledge Check | Multiple Choice

_Description_: Select the best answer.

_Prompt*_: What is printed on the screen after the following code is evaluated? Suppose that `list.pop()` removes the last (highest-index) element of the list and returns it.

```
summands = [3, 8, 1, 7]             # Line 1

total = 0                           # Line 2
while summands:                     # Line 3
    total = total + summands.pop()  # Line 4
    total = total - len(summands)   # Line 5

print(total)                        # Line 6
```

_Choices:*_

1. `[3, 8, 1, 7]`
2. `19`
3. `13` *
4. `9`

_Explanation*_: While `summands` is non-empty, the `while` loop continually adds the last element to `total`, removes the last element from `summands`, then subtracts the new list length from `total`.

Let's evaluate Line 3. `summands` has 4 elements so it is non-empty and hence `True`. So, we evaluate the indented lines. To evaluate Line 4, we must first evaluate `summands.pop()`. This returns `7` and removes `7` from `summands`. So Line 4 becomes `total = 0 + 7`. Since `len(summands)` is now `3`, Line 5 becomes `total = 7 - 3`. 

After this first iteration, now `total` is `4` and `summands` is `[3, 8, 1]`. Now, we go back and evaluate Line 3 again. Continuing in this manner, we effectively add all of the elements of `summands` to `total` and subtract the lengths `3`, `2`, `1`, and `0`. The final value of `total` is `13`. (Make sure you can run through each line of code just as the computer does!)

If you still find this question to be a bit tricky to understand, try copying the function into repl.it and placing a `print total` after `Line 4` and `Line 5`. This will allow you to see how `total` changes through each operation.  

----------------------------------
-->
## For Loops
 
### The `for` loop makes looping easier, provided that we can provide logic that will control when to stop thee `for` loop

----------------------------------

## Looping Through a List Using `for`

#### Let's see how easy it is to loop through the primes list from before:

```
primes = [1, 2, 3, 5]                  # Line 1

for prime_number in primes:            # Line 2
    print(prime_number)                # Line 3

print('Done!')                         # Line 4
```

- In this example, `prime_number` is an arbitrarily chosen name — it could just as easily be `prime` or even `x`. Each time we loop, this variable references the next element in `primes`, until no elements are left.

- Let's see how this works
  - When Line 2 is evaluated, `prime_number` is set to the first element of primes, `primes[0]`. Effectively, it sets `prime_number = primes[0]`. Because Line 3 is indented, it is evaluated next and `prime_number`, i.e., `primes[0]`, is displayed.
  - Next, we loop back to Line 2. Here, `prime_number` is set to the next element of primes, `primes[1]`. On Line 3, we display `prime_number` again.
  - This continues, until we loop back to Line 2 and we have iterated through each element in `primes`. At this point, the `for` loop is done and we jump to the next line after the code block, Line 4.

----------------------------------

The `for` Statement

#### The `for` statement always has the following structure:

```
for <variable name> in <sequence>:
	<indented line of code>
	...
```

- The _variable name_ can be **anything**. However, do not write over any of your other variable names!

- The _sequence_ is any object that can be iterated over. For example: lists, strings, tuples, dictionaries (the keys), and sets (though in no particular order!).

> **Reminder:** Notice how a colon always requires that at least the next line of code will be indented!
<!--
----------------------------------

> Knowledge Check | Multiple Choice

_Description_: Select the best answer.

_Prompt*_: The following code has a lot of bad variable names, making it tough to read. To make this code as clear as possible, which of the following variable names best clarifies the meaning of `x`?

_Hint: Copy the code block into a repl or text editor and replace the variable names with names the make sence to you._

```
s = 'The squirrel took a nut from a hole in the ground.'
x = 0

for c in s:
    if c == 'a':
        x += 1    
```

_Choices:*_

1. `total`
2. `total_letters`
3. `num_a` *
4. `extra_chars`

_Explanation*_: Let's rename `s` to `sentence` and `c` to `character`. Then, for each character in the sentence, we add one to `x` only if the current character is an `a`. So, the best name for `x` is `num_as`! (The name `total` is too vague.) Remember, programmers often use the variable name `num_cookies` to represent "number of cookies". 
-->
----------------------------------

_Slide Title:_ The `for` Statement, Cont.

_Slide Content:_

Let's look at another example:

```
# Sum N = 0,..,5
total = 0                           # Line 1
for num in [0, 1, 2, 3, 4, 5]:      # Line 2
    total += num                    # Line 3

print(total)                        # Line 4
```

- This sums the integers in the list. First, `total` is `0`. In Line 2, `num` is set to `0`, the first element in the list. In Line 3, `total = total + num`, so `total = 0 + 0`. 

- At the end of the code block, `total` is `0`. We loop back to Line 2. Now, `num` is set to the second element, `1`. In Line 3, `total = total + num`, so `total = 0 + 1`.

- Finally, we see that `total` is `15`, as expected!

**Pro Tip:** Python's built-in function `sum([0, 1, 2, 3, 4, 5])` accomplishes the same objective of the be above for loop.

----------------------------------


##`range`

#### It was really cumbersome having to write the integers from 1 to 5! What if we wanted to sum the first 100 integers? Python gives us a  built-in function that does this, called `range()`.

- `range(100)` returns a list of integers from `0` up to (but not including) `100`. (For a total of 100 - 0 = 100 elements.)
- `range(11,100)` returns a list of integers from `11` up to (but not including) `100`. (For a total of 100 - 11 = 89 elements.)
<!--
> In Python 2, `range(N)` actually generates a list, and `xrange(N)` returns a generator, which is more efficient but harder to think about! (In fact, it is beyond the scope of this tutorial.) In Python 3, `range(N)` also returns a generator. To create a list from a generator, just use `list()`, e.g. `list(xrange(N))`.
-->
----------------------------------

## Using `for` With `range`

#### Let's rewrite the earlier example to use `range`.

```
# Sum the first 100 integers
for num in range(101):
    total += num 
```

Remember, `range(N)` creates a list of integers from `0` up to but not including `N`. So, to sum the first 100 integers, we must set `N` to `101`.


--------------------------------

_Slide Title_: Lesson Demo

_Slide Content_:

[For a brief demonstration, check out the following short video.](https://generalassembly.wistia.com/medias/1aocklxk6p?embedType=async&videoFoam=true&videoWidth=640)


----------------------------------

##

+ How to create and use `if`/`else` statements.
+ How to create and us `while` statements.
+ How to create and us `for` loops.

<!--
**End-of-Lesson Quiz**

The following three-question quiz is designed to help you assess your knowlege of the above learning objectives.



----------------------------------

_Description_: Select the best answer.

_Prompt*_: What is printed after evaluating the following code?

```
jobs = ['CEO', 'data scientist', 'instructor']  # Line 1

if jobs:                  # Line 2
    if 'Pilot' in jobs:   # Line 3
        print(jobs[0])    # Line 4
    else:                 # Line 5
        print(jobs[1])    # Line 6
else:                     # Line 7
    print(jobs[2])        # Line 8
```

_Choices:*_

1. `CEO`
2. `data scientist` *
3. `instructor`
4. Nothing is printed.

_Explanation*_: `jobs` is non-empty, so it evaluates to `True` on Line 2. Next, `Pilot` is NOT an element of `jobs`, so the next `if` statement evaluates to `False` on Line 3. Hence, the `else` indented block is evaluated, starting on Line 6. (This prints `data scientist`!) Now, we jump to the next line following the `if` statement on Line 3. There is none, so we jump to the line following the `if` statement on Line 2. Again there is none, so we end execution. 

----------------------------------

_Description_: Select the best answer.

_Prompt*_: What is stored in `x` after evaluating the following code?

```
x = 1

while x < 1000:
    x = x * 2
```

_Choices:*_

1. The largest power of 2 less than 1000
2. The smallest power of 2 greater than 1000 *
3. `1000`
4. The first even number greater than 1000

_Explanation*_: In each iteration, `x` is doubled. So, `x` is always a power of 2. Note that we only exit the `while` loop if `x` is at least `1000`! So, `x` must be a power of 2 greater than `1000` for us to exit the `while` loop.

----------------------------------

_Description_: Select the best answer.

_Prompt*_: We notice that sometimes the wrong sum is displayed. The code has at least one bug — check all of the bugs.

_Hint: Pay close attention to the datatypes used._

```
summands = (2, 8, -1, 1, 9)

# Sum all the numbers up to -1 but not beyond
total = 0
for summand in summands:
    total += summand
    if summand == -1:
        break          # This keyword immediately exits the for loop

# Should be 2 + 8 = 10, since -1 is in the third position.
print(total)
```

_Choices:*_

1. When `summand` is -1, it is added to the total. Move the addition statement after the `if` statement. *
2. The `for` loop is an infinite loop.
3. `summands` is a set, which has no guaranteed order. It should be a `list`. *
4. `summands` is not a valid set since all data types are not the same.

_Explanation*_: First, if `summand` is -1, we want it to immediately exit the loop without adding -1 to total. Here, it adds -1 to total then exits the loop. Second, `summands` is a set, which has no guaranteed ordering. So, looping through it may return a different order each time or on different interpreters. Because our scheme depends on order, we should change this to a `list` instead. Note the `for` loop is not infinite, because `summands` is finite. 
--> 
----------------------------------

_Slide Title_: Additional Resources

_Slide Content_:

If you're interested in gaining more practice with this topic, check out the following resource:

- [Datacamp: Python Data Science Toolbox (Part 1)](https://www.datacamp.com/courses/python-data-science-toolbox-part-1). Specifically, see "Section 3. Lambda functions and error-handling," and complete the "Introduction to Error Handling" portion.

----------------------------------
