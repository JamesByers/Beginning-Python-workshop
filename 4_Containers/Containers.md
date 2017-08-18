
##### DF2: Python for Data Science
# Containers

## By the end of this section you will be able to

+ Demonstrate how to look up what is built into Python
+ Define lists, tuples, sets, and their common methods
+ Differentiate between lists and dictionaries

----------------------------------
<!--
_Slide Title_:  Core Python: Small Yet Powerful

_Slide Content_:

While you're learning to code with Python, don't be dissuaded if it seems like we're pulling new names from out of nowhere. In actuality, there's only a small set of components you'll use at any given time:

1. Keywords 
2. Built-in functions
3. Built-in data types (and associated methods)
4. Explicitly imported names from modules

Programming is the art of using this small set of data types, keywords, and functions to express thoughts. And, using only Python's built-in data types, keywords, and functions, you can actually implement **any** algorithm that operates on in-memory data. 

So far, we've only discussed Python's primitive data types, but it is worth knowing about the others so you understand that there are actually very few.


----------------------------------

_Slide Title_:  1. Keywords

_Slide Content_:

**Keywords** are specific reserved words that have special meaning to Python. Here's the [entire list of keywords in Python 3](https://docs.python.org/3/reference/lexical_analysis.html#keywords):

| --- | --- | --- | --- | --- |
| --- | --- | --- | --- | --- |
| `False` | `class` | `finally` | `is` | `return` |
| `None` | `continue` | `for` | `lambda` | `try` |
| `True` | `def` | `from` | `nonlocal` | `while` |
| `and` | `del` | `global` | `not` | `with` |
| `as` | `elif` | `if` | `or` | `yield` |
| `assert` | `else` | `import` | `pass` | |
| `break` | `except` | `in` | `raise` | |

----------------------------------

You likely already recognize many of these or can at least guess what they do. For now, just keep in mind:

+ There are very few keywords, and they are not complicated.
+ Keywords cannot be used as variable names!
+ Using these keywords might require a special syntax. For example, `if` must be followed by a valid expression, which must be followed by a colon.

> **Explore.** Try typing `if = 5`. You will get a **syntax error** — i.e., an error concerning the precise ordering of text. Here, Python expects an expression to follow the `if`, but `=` by itself is not a valid expression.

----------------------------------

> Knowledge Check | Multiple Select

_Description_: Select all that apply.

_Prompt*_:  Which symbols below would Python interpret as keywords?

```python
def triple(num):
    """ Returns the number multiplied by three. """
    
    total_is = 0
    for _ in range(3):
        total_is += num
    
    return total_is
```

_Choices:*_

1. `def` *
2. `triple`
3. `num`
4. `total_is`
5. `is`
6. `for` *
7. `_`
8. `in` *
9. `range`
10. `3`
11. `return` *

_Explanation*_: Remember back to our list of keywords. `total_is` contains the keyword `is`, but, because it is not an exact match, it is not a keyword in itself. The words `num`, `_`, `total_is`, `range`, and `triple` are all variable names that have values assigned to them. We will discuss these next! 

**Pro tip:** `def` is a keyword that acts as no more than an assignment, similar to `x = 5`. It creates a function object, then assigns it to the name `triple`.

----------------------------------

_Slide Title_:  2. Built-In Functions

_Slide Content_:


Python comes with a small-yet-powerful set of [built-in functions](https://docs.python.org/3/library/functions.html). Surprisingly, all you need to implement any algorithm is these functions (along with keywords and built-in data types). Keep in mind that:

- There are not many built-in functions, and you can easily guess what most accomplish.
- Each built-in function is simply a name that points to a function object.
- We've already seen a lot of these — e.g., `dir`, `type`, and the constructor function for each data type (`int`, `float`, etc.).

> We already discussed data types (#3), so now we'll move on to modules.

----------------------------------

_Slide Title_:  4. Modules

_Slide Content_:

In Python, you can't use an undefined name without defining or importing it first. For example, you cannot call the math module's `sin` function without importing it.

Imports typically go at the very top of your script or Jupyter notebook. If you see an unfamiliar name that is not built in, then it is nearly always the result of an import at the top of the file.

There are three typical ways to import in Python. An easy way to remember them is that, whatever comes after the keyword `import` is the name that will be defined in your code.

- `import math`: This imports everything in the `math` module under the name `math`. To access any math functions, you would call them using the method notation, e.g. `math.sin(0)`.
- `from math import sin`: This imports only the `sin` function from the `math` module. To use the `sin` function, simply call `sin(0)`.
- `from math import *`. This imports every function in the `math` module as its own name. This is considered bad practice, because it's unclear which names have been added by just looking at the `import` statement. It would be easy to accidentally overwrite one of these imported names.

----------------------------------

_Slide Title_:  Learning Objectives

_Slide Content_:

**Define Lists, Tuples, Sets, and Their Common Methods**

In this section, we will look at the **built-in containers**. A **container** is simply a data type that can hold more than one object.

----------------------------------
-->
## Lists

Suppose we have three types of animals. One way of storing the animal types is by using three separate variables:

```
animal_type1 = 'bird'
animal_type2 = 'giraffe'
animal_type3 = 'monkey'
```

As you might guess, this gets to be cumbersome. We will have difficulty storing more animal types in the future and looking through the animal types that we have! Lists help with this.

```
animal_types = ['bird', 'giraffe', 'monkey']
```

> As expected, `type(animal_types)` evaluates to `list`.

----------------------------------

## Lists, cont.

Here are some important points to remember about lists:

- Lists are **ordered**. Their elements have a particular order that will never change.
- Lists are **heterogeneous**. Different data types can be stored for each element of the list. For example, `['dog', 10, 0.4]`.
- Lists are **mutable**. When you alter a list, you don't create a new object — the original object is just modified.

Typically, the name of a list should be plural. For example, `cars`, `animal_names`, and `cities`. This immediately indicates that the name refers to a container.

----------------------------------
<!--
## Lists, Cont.

_Slide Content_:

```
animal_types = ['bird', 'giraffe', 'monkey']
```

- Recall that `len()` is a built-in function that takes any container as a parameter. So, `len(animal_types)` is `3`.

- Similar to strings, we can use the indexing operator (`[]`) to access any particular element in the list. So, `animal_types[0]` is `'bird'`.

- Unlike strings, we can set any element to a new value. For example, `animal_types[0] = 'cat'` replaces `'bird'` with `'cat'` as the first element.

----------------------------------
 
> Knowledge Check | Multiple Choice

_Description_: Select the best answer.

_Prompt*_: Suppose `dogs = ['Collie', 'Pug', 'Grand Shepard']`. What is `dogs[len(dogs)-2]`?

_Choices:*_

1. `'Collie'`
2. `'Pug'` *
3. `'Grand Shepard'`
4. `IndexError: list index out of range`


_Explanation*_: First, the inner expression is evaluated. We know `len(dogs)` is `3`, so `len(dogs)-2` is `1`. We look up `dogs[1]` and find that `'Pug'` has an index of `1`. This is not an `IndexError` because `1` is a valid index.

----------------------------------

_Slide Title_:  Literals

_Slide Content_:

In general, a **literal** is a text representation of a particular data type. When the text is interpreted by Python, this representation is converted into the 1s and 0s of the actual object. For example, `'I live in a city.'` is a "string literal." However, `I live in a city` does not represent a string — it's simply names Python will look up to find the objects to which they are referring.

Note that brackets have two meanings in Python:

- **If a bracket does not immediately follow an object or name, it represents a list.** This is called a "list literal" — a text representation of a list. For example, `days = ['Monday', 'Tuesday']`.

- **If a bracket immediately follows an object or name, it indexes into the object.** For example, `days[0]` indexes into the list referenced by the name `days`. 

In `print(['Monday', 'Tuesday'][0])` we find both uses of a bracket — as a literal AND an index. Because the list literal is converted to an object, the second use of brackets indexes into that object.

----------------------------------

> Knowledge Check | Multiple Choice

Description_: Select the best answer.

_Prompt*_:  What will happen when Python evaluates the following: `[0]`?

_Choices:*_

1. `TypeError`, because it indexes into `None`, which is not a container.
2. A new list is created containing a single element, 0. *
3. `IndexError`, because the 0th index of an empty string does not exist.
4. A new list is create with a length of 0.


_Explanation*_: These brackets do not immediately follow an object or name, so this is a list literal. Hence, Python will create a new list containing a single integer, 0.

----------------------------------
-->
## List Methods

Like before, we can view the methods available to a list object using the built-in function `dir()`. Alternatively, press `tab` after typing a period following a list object — e.g., `[1, 2, 3].` (if using `ipython`). The most important list method is `append()`, which adds a new element to the end of a list. For example:

```
animal_types = ['bird', 'giraffe', 'monkey']
animal_types.append('turkey')
```

After evaluating both lines, `animal_types` contains four elements: `['bird', 'giraffe', 'monkey', 'turkey']`.

----------------------------------

## List Methods cont.

- To sort the list, try `animal_types.sort()`.
- To remove the last element and return it, try `animal_types.pop()`.
- To reverse it, try `animal_types.reverse()`.
- To extend it using another list, try `animal_types.extend(['porcupine', 'dog'])`.

**Note:** Unlike string methods, these alter the original list! 
<!-- You may be wondering _why_. It's because the primitive data types in the last lesson — Booleans, numbers, strings — are **immutable**, and an immutable object never changes its value. Instead, the interpreter creates a new object and directs the name to it. For example, evaluating `312 + 457` actually creates a new `int` object, `769`! On the other hand, the methods of most containers (excluding strings and tuples) alter the same object for efficiency's sake. The language designers decided to not return a list to emphasize to the programmer that lists are **mutable** — the original was changed! This prevents you from making common mistakes.
-->

----------------------------------

## Tuples

### The name tuple is meant to be a shorthand for fixed and predetermined data meanings
Tuples are similar to lists in that they are containers of objects. However, there are two main differences:

- They are defined using parentheses instead of brackets.
- They are **immutable** — you cannot alter a particular tuple object once it is created. So, most methods such as `append()` and `pop()` do not exist.

You can define a new tuple like so:

```
# (month number, month name, num days)
month = (1, 'January', 31)
```

----------------------------------

## List vs. Tuples

### uideline:
- Use lists when order is important and adding elements is expected
- Use tuples when order is not significant, the elements collectively represent something, and the contents are never changed

For example, suppose we have a computer defined by a name, amount of RAM, and date of manufacture.

```
my_computer = ('WORK_COMPUTER', 8, 2017)
```

Here, it is not meaningful that the computer name comes before the RAM amount. The order could have just as easily been defined differently without consequences. If we are alright with never being able to alter it's contents is best represented as a tuple.

----------------------------------

## List vs. Tuples, cont.

Next, suppose we have a list ordered by most-used computer.

```
most_used_computers = ['WORK_COMPUTER', 'HOME_COMPUTER', 'LAPTOP']
```

Because these are all strings (homogeneous) and order matters, this is best represented as a list.

> You may be wondering why we would use tuples if they are actually more restrictive than lists. Making a data type immutable allows it to be more efficiently represented in memory. Furthermore, immutable types can be used in some additional objects (such as keys to dictionaries).

----------------------------------
<!--
> Knowledge Check | Multiple Choice

_Description_: Select the best answer.

_Prompt*_: Suppose we have a container of computers. According to our earlier suggestions, what should be changed to best represent it?

```
computers = (('WORK_COMPUTER', 8, 2017), ('HOME_COMPUTER', 16, 2016), ('LAPTOP', 8, 2016))
```

_Choices:*_

1. `computers` should be a list of tuples. *
2. Each individual computer should be a list, not a tuple.
3. `computers` should be a list of lists.
4. Nothing is wrong.

_Explanation*_: Although the order of the computers may or may not be significant, each computer is of the same data type. Also, we could easily see another computer being appended at some point in time. So, `computers` should be a list. Each individual computer should be a tuple, as we discussed previously.

----------------------------------

## Sets

#### A set is a collection of unordered, unique elements. For example, two people may have watched different sets of movies.

```
my_movies_watched = {'Aladdin', 'Dumbo', 'Beauty and the Beast'}
your_movies_watched = {'Wizard of Oz', 'Aladdin'}
```

In this case, the particular order inside the set does not matter, as each movie was either watched or it wasn't. Note that Python knows these are sets because the strings are surrounded by curly braces and only contain a simple container of elements, which are separated by commas.

> **Pro tip:** To create an empty set, you must use the built-in `set()` function. For example, `untasty_fruits = set()`. Why? Because to Python, curly braces are used for both sets and dictionaries. Empty braces `{}` indicate an empty dictionary.

----------------------------------

_Slide Title_:  Sets

_Slide Content_:

Sets have two important methods — intersection and union. The **intersection** of two sets is the set of all elements common to both of them.

```
our_movies_watched = my_movies_watched.intersection(your_movies_watched)
# {'Aladdin'}
```

The **union** of two sets is the set of all elements in either of them.

```
all_movies_watched = my_movies_watched.union(your_movies_watched)
# {'Dumbo', 'Aladdin', 'Beauty and the Beast', 'Wizard of Oz'}
```

To add a new object to a set, use the `add()` method, e.g., `my_movies_watched.add('The Little Mermaid')`.

----------------------------------

_Slide Title_:  Sets

_Slide Content_:

Important points about sets to remember include:

- **Sets are unordered.** Never use a set if order matters!
- **Sets contain no duplicate elements.** `{1, 2, 2}` is equivalent to `{1, 2}`.
- **Membership lookups are fast.** Determining whether or not an element is included a set often takes a constant amount of time.

To find out whether or not a set contains an element, use the `in` operator: `'Aladdin' in my_movies_watched` evaluates to `True`.

----------------------------------
 
 > Knowledge Check | Multiple Choice

_Description_: Select the best answer.
 
_Prompt*_: Suppose you are implementing a spell checker. For each word, you will test whether or not the word is contained inside a list (or set, or string!) of known words. What is the best data structure in which to store the words? Why?

```
valid_words = ['car', 'soup', 'zebra', ...] # list implementation
valid_words = ('car', 'soup', 'zebra', ...) # set implementation
valid_words = 'car\nsoup\nzebra\n...' # string implementation
```

_Choices:*_

1. List, because words are all the same data type and have an alphabetical order.
2. Set, because the words' order in the set is not important for a spell checker, and membership lookups are fast.*
3. List, because the index of each word is important.
4. String, because each word is a string, so storing the words in a simpler data type is fast.

_Explanation*_: In this case, a set is preferable to a list, because testing for membership is faster for sets. Each word will be unique in the set, and a word's position in the set does not matter for a spell check (only that it is contained in the set). Additionally, the variable name we are assigning to `'valid_words'` also tells us a little about the nature of its contents. Note that elements of the same data type are typical in both lists and sets (although technically this is not required). Storing the words in a large string is possible, but it would be inefficient to search for a word, and this doesn't abstract their structure well.

----------------------------------
-->

## How Dictionaries differ from lists 

#### Dictionaries represent key-value pairs. For example:

- Names could be paired with ages.
- Months could be paired with the number of days in the month.
- Book titles could be paired with authors. 

In this section, we will look at how to define dictionaries, as well as some common use cases.

----------------------------------

## Dictionaries

#### Similarly a dictionary is defined using curly braces

- Each element of a set consists of a key, followed by a colon, followed by a value. So, the presence of colons can be used to distinguish between a "set literal" and a "dictionary literal". For example:

```
book_authors = {'Moby Dick': 'Herman Melville', 'Green Eggs and Ham': 'Dr. Seuss', 'The Great Gatsby':  'F. Scott Fitzgerald'}
```

Notice this is a container of **key-value pairs**. So, `len(book_authors)` is `3`, as there are three key-value pairs.

----------------------------------
<!--
## Dictionaries, cont.

Alternatively, you can think of a dictionary as a generalized list! Instead of indexing items by integers, we now index them by their keys. For example: `book_authors['Moby Dick']` evaluates to `'Herman Melville'`.

The keys can be any immutable data type, while the values can be any data type. For example:

`points_grades = {0: ['Fail', 'F'], 10: ['Perfect', 'A+']}`

Then, a student receiving 10 points would get the grade `points_grades[10]`, which would evaluate to the list `['Perfect', 'A+']`.

To add a new key-value pair to the dictionary, index into a new key: `book_authors['The Jungle'] = 'Upton Sinclair, Jr.'`. This adds a new key, `'The Jungle'`, with a value of `'Upton Sinclair, Jr.'`. 

----------------------------------
-->
## Dictionaries, cont. 

Another way of thinking about a dictionary is as a set of keys and a list of values. The container of keys must be a set, because each key is unique (i.e., has at most one value). With this in mind, two useful dictionary methods are:

- `book_authors.keys()` — to convert it to a set, you can use the built-in `set()` function.
- `book_authors.values()`

You should realize that a dictionary is **unordered** and therefore that the key-value pairs do not exist in any particular order.

----------------------------------

## Review: Container Data Types

#### Let's review the properties of the data types we discussed in this lesson — the built-in containers.

| --- | Lists | Tuples | Sets | Dictionaries |
| --- | --- | --- | --- | --- |
| Container | Yes | Yes | Yes | Yes |
| Ordered | Yes | Yes | - | - |
| Immutable | - | Yes | - | - |
| Elements must be unique | - | - | Yes | Yes (keys only) |
| Fast membership lookups | - | - | Yes | Yes (keys only) |

----------------------------------
<!--
_Slide Title_: Lesson Demo

_Slide Content_:

[Next, check out the following video for a brief demonstration.](https://generalassembly.wistia.com/medias/u360zquzcm?embedType=async&videoFoam=true&videoWidth=640)

--------------------------------
-->

## Practice

#### Ready for some practice?  Try your hand at the following challenges. 

Open the [containers_practice.py](https://github.com/JamesByers/GA_Python_for_Data_Science_workshop_08_2017/raw/master/4_Containers/containers_practice.py) file in Spyder and give these a try:

1. Create a `list` called `my_list` and store the values `3,20,"hello","goodbye"` within it.

2. Print the list in reverse.

3. Add `4.3` to the list.

4. Remove `3` from the list.

5. Create a dictionary called `week_dict` that stores the days of the week as keys and whether or not they are part of the weekend as values.

6. Collect all of the weekdays into a list.

7. Delete `Monday` from `week_dict`.

--------------------------------
<!--

_Slide Title_: Lesson Practice Solutions

_Slide Content_:

Have you finished practicing? Next, check your work against our suggested solutions below:

## Open up [Repl.it](https://repl.it/languages/python) and complete the following:

1. Create a `list` called `my_list` and store the values `3,20,"hello","goodbye"` within it.

		my_list = [3,20,"hello","goodbye"]
        
2. Print the list in reverse.

		print(my_list[-1::-1])

3. Add `4.3` to the list.

		my_list.append(4.3)
        
4. Remove `3` from the list.

		my_list.remove(3)
        
5. Create a dictionary called `week_dict` that stores the days of the week as keys and whether or not they are part of the weekend as values.

		week_dict = {"Monday":False,"Tuesday":False,"Wednesday":False,"Thursday":False,"Friday":False,"Saturday":True,"Sunday":True}
        
6. Collect all of the weekdays into a list.

		week_dict.keys()
        
7. Delete `Monday` from `week_dict`.

		del week_dict["Monday"]


----------------------------------
-->
## Containers Review

Now you will be able to:

+ Look up what is built into Python
+ Define lists, tuples and their common methods
+ Describe the differences between lists and dictionaries
<!--
**End of Lesson Quiz**

The following quiz is designed to help you assess your knowlege of the criteria above.


----------------------------------

_Description_: Select the best answer.

_Prompt*_: Suppose we have a large list containing categories of houses. How might we determine the number of unique categories? For example:

```
# contains 3 unique categories
house_categories = ['Single-Family Home', 'Condo', 'Condo', 'Duplex', 'Condo']
```

_Choices:*_

1. `house_categories.count()`
2. `len(list(house_categories))`
3. `set(house_categories)` 
4. `len(set(house_categories))` *

_Explanation*_: Converting the list to a set using `set(house_categories)` removes all duplicate elements. Then, computing the length of this set provides the number of unique elements.

----------------------------------

_Description_: Select the best answer.

_Prompt*_: Suppose we set `month = 12`, as December is the 12th month. What does `days_in_month[month]` evaluate to?

```
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
```

_Choices:*_

1. `31`
2. `30`
3. `28`
4. `IndexError: list index out of range` *


_Explanation*_: This is an example of an "off-by-one" error. Because Python uses zero-based indexing, the last element of `days_in_month` has index 11 — despite `len(days_in_month)` being 12. So, the coder should have written `days_in_month[month-1]`. As it is, the index `12` does not exist, so an `IndexError` will be thrown.

----------------------------------

_Description_: Select the all that apply.

_Prompt*_: Suppose you see the name `xyz` in a script and it is a valid name. Given your knowledge of where names come from in Python and the contents of some of the categories below, check the smallest set of possible places where `xyz` could have been defined.

_Choices:*_

1. Defined in the script *
2. Keyword
3. Built-in function
4. Built-in method
5. Built-in data type
6. Imported from a module with a line in the script *

_Explanation*_: The symbol `xyz` is meaningless, so it cannot be a keyword or a built-in function in Python. Hence, it must have either been defined in the script or imported at the top of the script. There is no other way for the name to be valid.

----------------------------------

_Description_: Select the best answer.

_Prompt*_: What would be the result of evaluating the following code?

```
len({3, 2, 9, 5, 3, 6, 2}) + len([3, 2, 9, 5, 3, 6, 2])
```

_Choices:*_
1. `7`
2. `10`
3. `12` *
4. `14`

_Explanation*_: A set does not contain duplicate values. So, the set contains a total of `5` unique values, while the list contains a total of `7` values. Summed together, this is `12`.



----------------------------------

_Description_: Select the best answer.

_Prompt*_: What is the most likely result when evaluating the following code?

```
set([1, 1, 3, 8, 9, 10])[0]
```

_Choices:*_
1. `TypeError`: `'set'` object does not support indexing *
2. `1`
3. `3`
4. `10`

_Explanation*_: This is a `TypeError`, as sets are unordered. Hence, they would have no first element. (After all, if there were a first element, then the set must have an order!)

----------------------------------

_Description_: Select the best answer.

_Prompt*_: Suppose we are building a service in which a user enters two city names and we provide the number of miles between them. Which of the refactors of the code below uses the most appropriate and scalable data types? Suppose speed of lookup is the most important factor. (You can assume we put the two city strings in alphabetical order before indexing into the data type.)

```
node1 = 'Los Angeles'
node2 = 'London'
node3 = 'NYC'
dist_node1_node2_miles = 5437
dist_node1_node3_miles = 2789
dist_node2_node3_miles = 3459
```

_Choices:*_

1. `cities = ['Los Angeles', 'London', 'NYC'], cities_dist_miles = [(0, 1, 5437), (0, 2, 2789), (1, 2, 3459)]`
2. `dist_cities_miles = {('London', 'Los Angeles'): 5437, ('Los Angeles', 'NYC'): 2789, ('London', 'NYC'): 3459}` *
3. `city_pairs = [['London', 'Los Angeles'], ['Los Angeles', 'NYC'], ['London', 'NYC'])], dist_miles = [5437, 2789, 3459]

_Explanation*_: All three methods work. However, the two list-based data types require two variables to represent the distance. Additionally, looking up the city pairs would be slower in each, as they do not use sets. So, the dictionary is the best option. You can consider the two cities to be the key and the distance between them to be the value. Tuples are immutable, so they can be used as dictionary keys.
-->
----------------------------------

## Additional Resources

### If you're interested in gaining more practice with this topic, check out the following resources:

- [Datacamp: Intro to Python for Data Science](https://www.datacamp.com/courses/intro-to-python-for-data-science), specifically Section 2: "Python Lists."

- [Hacker Rank, Python Challenges](https://www.hackerrank.com/contests/data-fundamentals-ga/challenges/python-lists): try this challenge on creating lists in Python.

----------------------------------
