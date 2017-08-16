###### Python for Data Science workshop
# Data Types

## Introduction to Python

The creator of Python wrote that the name Python originated from ____?

**Choices:**

1. The snake genus Python
2. Monty Python's Flying Circus
3. The mathematical constant pi
4. An earlier programming language Py
<!--
_Explanation*_:  "I chose Python as a working title for the project, being in a slightly irreverent mood (and a big fan of Monty Python's Flying Circus)." — [Guido van Rossum](https://en.wikipedia.org/wiki/Python_(programming_language)#History)
-->

----------------------------------
## Learning Objectives


#### By the end of this lesson you will be able to...
 
+ Demonstrate how to assign and manipulate variables.
+ Define primitive Python data types and common use cases (e.g., int, float, str).
+ Utilize basic string indexing and built-in methods.

----------------------------------

## Why Is Python Useful for Data Science?

+ **Open source** - You are not locked into using a particular company's products.
+ **Large community** - Easily find answers to questions.
+ **Interpreted** - Code can be run piece by piece, without creating an executable file.
+ **Abundance of third-party packages** - Prewritten Python packages can be used for data science, video games, website backends, computer vision, and more.
+ **Easy C integration.** - Speed-critical routines can be written in the low-level language C and easily integrated.

----------------------------------

<!--
_Slide Title_:  When Might You Not Use Python?

_Slide Content_:

+ When high performance or low memory usage is important.
+ If direct access to hardware is required.
+ When OS-specific GUI features are desired.
+ In embedded systems programming, where speed and memory footprint matter.

----------------------------------


_Slide Title_:  How a Computer Program Works

_Slide Content_:

Computer programs have three general steps:

1. **Load data from the outside world into memory.** This involves loading data into variables, which are typically stored in your main memory (RAM). This data could come from a file, database queries, API calls, keystrokes, mouse clicks, etc.

2. **Manipulate the data in memory.** Once data is stored in variables, it can be easily and efficiently accessed and manipulated by your Python script.

3. **Export the data back to the outside world.** Once your script does some processing, it must export the variables and store the result. This could be writing to a file, writing to a database, or lighting pixels on the screen.

Most programming books exclusively (and appropriately) focus on the second step. However, many students get lost making a "real" program from what they learn in books. Typically, they are only missing how to load data into variables, or how to export those variables back to disk or the screen!

----------------------------------

> Knowledge Check | Multiple Choice;

_Description_: Select the best answer.

_Prompt*_:  Which of the following is **least** an example of the three steps?


_Choices:*_

1. A video game reads in controller input, computes how the player moves, then renders the next frame to the screen.
2. A background script scrapes the latest news stories, automatedly summarizes each story, then writes the summaries to a database.
3. An app loads a user's notes from disk, sorts them so the latest note is on top, then displays them using the phone's native UI.
4. A program computes the first 100 prime numbers then displays them to the screen. *

_Explanation*_: Although this answer seems less like the others, it still follows the pattern — the program itself is data loaded from a disk into RAM! Notice that each of these examples is broken down into three steps. These steps are generally independent of one another. So, if you are ever stuck, you can enhance any one of the three.

----------------------------------

_Slide Title_:  Running Python

_Slide Content_:

In data science, we generally run Python in three ways.

1. **Interactively from the command line.** (`python` or `ipython`) This interactively allows the user to type and evaluate one line at a time. It is called a **REPL**, for Read, Evaluate, Print, Loop. It reads the user's input, evaluates it, prints the output, then loops back to prompting the user for input. This is useful for quickly experimenting with short code snippets.

> **Try it!** Throughout this guide, we will ask you to experiment with Python. You can do so in one of two options.
+ Using Repl.it (Recommended): Navigate to https://repl.it/languages/python, where you can easily type code, run, and see output in a user friendly environment. 

+ In the terminal: Open Terminal (Cmd-Space then type `Terminal`). Then, type `ipython` at the command prompt. Now, you can evaluate individual lines of code such as `1 + 1` by typing them and pressing `enter`.


----------------------------------

_Slide Title_:  Running Python, Cont.

_Slide Content_:

2. **As a script.** (`python <script_name>`) By saving Python code in a file, we can run it automatically. This is useful when writing complex programs or automated programs. We can also store frequently used routines in a file and import them in an interactive session.

3. **From a Jupyter notebook.** (`jupyter notebook`) Jupyter is also a REPL, but it allows us to easily save the input and output in a friendly way.

> **Pro tip:** The program `ipython` ("Interactive Python") was created as an enhancement over Python's bare-bones REPL. It adds useful features such as syntax highlighting and "magic commands" that begin with `%`. Jupyter notebook is actually built on top of IPython — it passes each input cell to `ipython` in the background and shows you the result!

----------------------------------

_Slide Title_:  Python Enhancement Protocols

_Slide Content_:


Python Enhancement Protocols, or PEPs, are documents that explain the _why_ behind each new Python feature. A new PEP must be written for the community to consider a new feature.

Here are some example PEPs:

+ [**PEP 8 — Style Guide for Python Code.**](https://www.python.org/dev/peps/pep-0008/) Ever wonder how many spaces to use, the maximum line length, or when to uppercase variables? Read this!
+ [**PEP 20 — The Zen of Python.**](https://www.python.org/dev/peps/pep-0020/) Every lanugage has an underlying philosophy. The gist of Python's is: Prefer readable slow code over hard-to-read performant code.
+ [**PEP 465 — A dedicated infix operator for matrix multiplication.**](https://www.python.org/dev/peps/pep-0465/) This more recent PEP explains the rationale behind adding a new Python 3 operator for matrix multiplication.

> **Easter egg:** Try running `import this`.

----------------------------------

> Knowledge Cjeck | Multiple Choice;

_Description*_: Select the best answer.

_Prompt*_:  Suppose you are writing a new Python file and write the below code, where the `print` statement is indented. [According to PEP 8](https://www.python.org/dev/peps/pep-0008/), when typing this in an editor, how should you indent the statement?

```python
if 1 + 1 == 2:
    print("As expected, 1 + 1 is 2.")
```

_Choices:*_

1. 2 spaces
2. 4 spaces *
3. 1 tab
4. 2 tabs

_Explanation*_: Spaces are often preferred because tabs can have inconsistent widths on different computers. This can cause code to not line up as expected. **Pro tip:** Many text editors, including Sublime Text and PyCharm, have options to automatically convert tabs to spaces as you type.

In Python, indentation is mandatory. If a line ends in a colon, at least the next line must be indented. For example, statements that begin with `if`, `for`, and `def` all end in a colon. So, they must be followed by at least one indented line.
-->

----------------------------------

_Slide Title_:  Learning Objective: 

_Slide Content_:

**How to Assign and Manipulate Variables**

In this section, we will discuss operators.

----------------------------------

_Slide Title_: Operators

_Slide Content_:


In Python, **operators** act on one or two objects and evaluate to a single object. For example:

- `1 + 1` evaluates to `2`.
- `'a' + 'b'` evaluates to `'ab'`.

An integer added to an integer evaluates to an integer. A string added to a string evaluates to a string.

> Make sure you actively try these yourself in the REPL. **Pro tip:** Behind the scenes, Python actually [converts each operator into a function call](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions)! For example, `'a' + 'b'` is evaluated as `'a'.__add__('b')`. The dot indicates we are calling a method of the `'a'` object. We will look at objects in more detail in Lesson 2!

----------------------------------

### Operators, Cont.

_Slide Content_:

It is important to know the data type on each side of the operator. This defines what the operator will produce. For example, think about what you might expect these to evaluate to, then try them out:

- `'a' * 3`
- `3 * 'a'`
- `'a' * 2.5`

The results of these operators do "make sense" given what we know about multiplication! In Python, many of the libraries were created by people to "make sense" in this way. So, we can usually guess what might work and be correct.

Note there is no "correct" answer about what these should output! The results of these operators acting on specific data types was decided on by a person. They could have just as easily been defined so that multiplying a string by an integer is nonsense and hence a syntax error! (In fact, this is the case in many languages such as C.)

----------------------------------

_Slide Title_: The Assignment Operator

_Slide Content_:

The assignment operator is a single equals sign (`=`). It associates a **name** with a value. For example:

- `num_cookies = 3`
- `first_name = 'Sally'`

The assignment operator is very different from the equals sign we are familiar with in math. Instead of asserting the two sides are equal, the assignment operator **defines** a name. It first evaluates the right-hand side, then associates the name on the left-hand side to the the result of the evaluation. The above two lines of code work as follows:

- An integer object is created with value 3. Then, we point the name `num_cookies` to it.
- A string object is created with value 'Sally'. Then, we point the name `first_name` to it.

----------------------------------

_Slide Title_: The Assignment Operator, Cont.

_Slide Content_:

Here is an example where newcomers often get confused:

```python
num_cookies = 3
num_cookies = num_cookies + 1
```

Clearly, `num_cookies` cannot be equal to one more than itself! However, recall that `=` is not a comparison, but a definition. So, we first evaluate the *right-hand side*, `num_cookies + 1`, to be `4`. Next, we point the name `num_cookies` to it.

--------------------------------

> Knowledge Check | Multiple Select;

_Description*:_ Select the best answer.

_Prompt*_:  Without trying it, what would you guess the following code produces? (Remember that if `title` was a positive integer instead of a string, `-title` would be a negative number!)

```python
title = 'Data Science'
title = -title
```

_Choices:*_

1. `ecneicS ataD`
2. `TypeError: bad operand type for unary -: 'str'` *
3. `data science`
4. `Data Science is awesome!`

_Explanation*_: Applying the `-` unary operator to a string sounds confusing as to what it might produce. After all, a string does not have a "negative" value like a number does. Although it is plausible that it would reverse the string, this does not sound like a very natural definition. So, it will likely produce a `TypeError`, aka not be a defined operation. This may sound a bit like an arbitrary question; however, good programmers often guess at what likely "makes sense" rather than memorizing everything. You will find that your guesses will eventually be very accurate.

----------------------------------

_Slide Title_: The Comparison Operator

_Slide Content_:


In Python, the equality sign from math class still exists — it is now the double equals `==`. This operator compares two objects and evaluates to either `True` or `False` only if the values are the same. For example:

- `2 == 2` -> `True`
- `2 == 3` -> `False`
- `'hi' == 'hi'` -> `True`
- `'hi' == 'bye'` -> `False`

It is important to note that `==` is an operator just like `+`. Compare the following:

- `num_cookies = 1 + 2` -> `3`
- `is_confirmed = 'yes'`  
  `is_confirmed == 'yes' -> 'True' `

> **Pro tip:** To combine multiple operators, use parentheses to avoid any possibility of ambiguity, e.g., `('1' + '2') == '12'`

----------------------------------

_Slide Title_: Learning  Objective:

_Slide Content_:

** Define primitive Python data types (e.g., `int`, `float`, `str`).**

We have already worked with a few data types, namely integers and strings. We saw that knowing the data type of each object is very important.

Recall that your computer stores everything in binary as 1s and 0s, whether it is integers or text characters. **Data types** tell the computer how to interpret these 1s and 0s. For example, the same sequence `01000001` can represent the integer `65` or the character `'A'`.

----------------------------------

_Slide Title_: Data Types

_Slide Content_:



Python comes with only a few data types. The complete list of built-in data types is: `None`, Booleans, Numbers (`int`/`float`/`long`/`complex`), Strings, Lists, Tuples, Sets, and Dictionaries.

Let's explore these data types further and play with them in the REPL!

> You can actually think about the data science libraries as merely adding new data types to Python — `ndarray` (NumPy), `Series` (Pandas), and `DataFrame` (Pandas).

----------------------------------

_Slide Title_: Integers

_Slide Content_:


- Whole numbers are integers, with an optional `+` or `-` prefix, e.g., `3`, `82`, `38218`, `+3`, `-71`. 
- In Python, integers can be as large as desired. For example, `27381732198731297381273127`.

**Be careful!** In Python 2, an integer divided by an integer is an integer. This way, all operations maintain the same data type. However, this is a common source of confusion for newcomers! For example, `2 / 3 = 0` and `5 / 2 = 2`. (It truncates the result, i.e. the (floored) quotient.

**Pro tip:** The `%` **modulus operator** returns the remainder.

> In Python 3, the above divisions produce floating point numbers. (Python 3 additionally adds the quotient operator `//`.)

> Try experimenting with the built-in function `type()`, e.g., `type(72)`.

----------------------------------

_Slide Title_: Floats

_Slide Content_:

- By default, decimal numbers are stored as **floating point** numbers. They are called floating point because they are internally stored using scientific notation, e.g., `3.5 x 10^10`. The position of the period "floats" up and down the number as the exponent changes.

- A period with a whole number before and/or after is interpreted as a float, e.g., `0.32`, `.32`, `83.7823`, `1.00`. 

- To divide two non-multiple integers, write them as `2. / 3.`, which will return a float. Alternatively, `float(2) / float(3)` converts the integers to floats before dividing.

> **Be careful!** Floating point numbers are stored using a limited number of bits, so they have numeric limits. For example, try `0.1 + 0.7 == 0.8`. It is `False`! Whenever comparing floats, you should be aware of this limitation. To compare whether `total` is "close to" `0.8`, you can use the following: `abs(total - 0.8) <= 0.000001`. (There is also a `closeto` function in the `math` module.)

----------------------------------

_Slide Title_: Boolean

_Slide Content_:


Boolean values are either `True` or `False`. Internally, they are stored as an integer which is `1` if `True` and `0` if `False`.

Boolean variables are often called **flags** since they indicate whether something is present. For example, `email_is_valid` could be a flag indicating a valid email address.

- When naming a Boolean variable, it is often helpful to prefix it with `is_` or `has_` to clearly show it is a flag. For example,  `has_header`, `is_first`, `is_blue`.

- Recall that the comparison operator `==` always evaluates to `True` or `False`!

----------------------------------

> Knowledge Check | Multiple Select;

_Description:_ Select the best answer.

_Prompt*_:  What are (respectively) the most reasonable data types for these variable names: `num_shoes`, `is_on`, `temp_fehrenheit`, `birth_year`?

_Choices:*_

1. `float`, `int`, `float`, `int`
2. `int`, `int`, `float`, `float`
3. `int`, `bool`, `float`, `int` *
4. `float`, `bool`, `int`, `int`

_Explanation*_: The number of shoes (`num_shoes`) is a discrete quantity that we would rarely, if ever, add a fraction onto. Hence, it would be an integer. `is_on` is likely either on or off, so a boolean. `temp_fehrenheit` could be an integer; however, it is likely that temperature could at some point be recorded with high accuracy, so it is a float. A year is never fractional, so `birth_year` is an `int`. 

> **Pro tip:** It is important to be as clear as possible when naming variables. Variable names should ideally communicate the data type, units, and specifics immediately from reading the variable name. For example, `year` does not communicate what year (the birth year). `temperature` does not communicate units (Fehrenheit). `shoes` would not be enough to inform us it is an integer.


----------------------------------

_Slide Title_: Strings

_Slide Content_:

A **string** is a sequence of characters. To indicate a string in Python code, enclose it with quotation marks. 

Single-quotes `'` and double-quotes `"` are equivalent in Python. If your string contains a single-quote, then enclose it with double-quotes, and vice versa. Examples:

- `first_name = 'Charles'`
- `html = '<a href="https://generalassemb.ly/"></a>'`

> Try `typeof('some text')`.

----------------------------------

_Slide Title_: Escape Characters

_Slide Content_:



Strings may also contain characters with special meaning. For example, a newline (`\n`), tab (`\t`), or special Unicode character.

To use these, prefix them with a backslash as shown above. You can enter a backslash as `\\`. For example:

- `'Line One\nLine Two'`
- `"A list:\n\t- Bullet 1\n\t- Bullet 2"`

To view these lines as intended without the backslashes, just print them, e.g., `print("A list:\n\t- Bullet 1\n\t- Bullet 2")`.

----------------------------------

_Slide Title_: Multi-Line Strings

_Slide Content_:


A third way of defining strings exists: the multi-line string. By enclosing text in three quotation marks (`"""` or `'''`), multi-line strings can be written that preserve newlines. For example:

```
"""
Header
	- Line Two
	- Line Three
"""
```

becomes: "\nHeader\n\t- Line Two\n\t- Line Three"


----------------------------------

_Slide Title_: Data Type Conversions

_Slide Content_:

Most built-in data types have a built-in function (a **constructor**) that assists with conversions. For example, we saw that `float(3)` creates a new `float` object. `str(72)` returns a string representation of the integer `72`. `bool(82)` returns `True` for any non-zero integer. `None`, `True`, and `False` do not have constructors since they are singular values.

----------------------------------

> Knowledge Check | Multiple Select;

_Description_: Select the best answer.
_Prompt*_:  What is printed to the screen in the following code?

```python
result = str(1) + str(2)
print(int(result) + 3)
```

_Choices:*_

1. `'123'`
2. `TypeError`
3. `6`
4. `15` *

_Explanation*_: First, the right-hand side of the assignment operator is evaluated. The integer `1` is converted to a string, and the integer `2` is converted to a string. Next, the two strings are added, resulting in `result` pointing to the string `12`. 

In the second line, `result` is looked up to be `12`. So, the second line can be considered as: `print(int(`12`) + 3)`. The string `12` is converted to an integer then summed with the integer `3`, making `15`.

Note that adding a string and an integer would have given a `TypeError`. (This is another language design choice — in other languages such as JavaScript, adding these types would not produce an error!)


----------------------------------

_Slide Title_: Learning Objective

_Slide Content_:

** Demonstrate basic string indexing and built-in methods.**

In this section, we will look at how to get individual characters of a string. We will also see how we can use built-in Python methods to manipulate strings.

----------------------------------

_Slide Title_: Indexing

_Slide Content_:


We noted earlier that a string is a sequence of characters. Hence, we should be able to get the value of any individual character. In Python, we do this using **zero-based indexing**, where the first character is referenced by index 0. So, the last character in the string would be referenced by one less than the number of characters.


We can use the `len()` built-in function on any Python object that might have a length. Here, the length of a string is the number of characters in it.

We can use the indexing operator `[]` to get a particular character in the string.

Suppose we are define `title = 'President'`. Then, `title[0]` is the character `'P'`. `len(title)` evaluates to `9` since there are nine characters in `'President'`. So, `title[8]` is the character `t` due to zero-based indexing. More generically, `title[len(title)-1] ` evaluates to `'t'`.

----------------------------------

_Slide Title_: Indexing, Cont.

_Slide Content_:


Since `title` is a name that just points to the `'President'` object, you can also index into a newly created string! For example, `'giraffe'[0]` evaluates to `'g'`. Here, a string object is created then it is indexed into. When we wrote `title[0]`, it looked up the object `title` pointed to then indexed into it.

Later, we will discuss **slicing**, an extension of indexing.

> **Explore:** What do you think might happen if you index by a negative number? What if you index by a number greater than the length of the string? Do your answers agree with the choices the Python language designers made?


----------------------------------

_Slide Title_: Everything Is an Object!

_Slide Content_:

In Python, you will hear that everything is an object. What does this mean? An **object** is just a particular grouping of functions and variables. The functions of an object are called **methods** — functions that "belong to" an object (and typically act on its variables).

For example, a string contains variables — the characters! It also contains methods that act on the string, for example `upper()` converts the string to uppercase. These methods are called by using a period after the variable name. 

For example: `'dog'.upper()`. This first creates a new string object, then it calls its `upper()` method. This function returns an object, in this case the upper-case string `'DOG'`. If you set `animal = 'dog'`, then you can all `upper()` the same way, `animal.upper()`. Here, it looks up the object that `animal` points to then calls its `upper()` method.

----------------------------------

_Slide Title_: Everything Is an Object!, Cont.

_Slide Content_:

To view what methods are available in a REPL or Jupyter, type: `'dog'.` (with a trailing period), then hit the `tab` key (only if you are using `ipython`). Alternatively, you can call the built-in function `dir()` (short for "directory"), e.g., `dir('dog')`. To see what each method does, call the `help()` function, e.g., `help('dog'.upper)`. You can also refer to the [documentation online](https://docs.python.org/3/library/stdtypes.html#string-methods). It is worth it for practice to try out each of the string methods, since you will be using them so often!

Try out some of the other string methods! Define a new string variable `name` containing your full name. Then, using the techniques above try out some of the available methods. In particular, try `name.capitalize()`, `name.title()`, `name.islower()`, `name.center(40)`, and `name.center(40, '*')`.

> **Pro tip:** Note that `'dog'.upper` is a name, too. It points to an object — a function object! Try: `type('dog'.upper)`. When Python sees an open parenthesis immediately following a name, it knows you must be making a function call.

----------------------------------

_Slide Title_: Lesson Demo

_Slide Content_:

[Want to see an example of these in-action? Check out our brief overview.](https://generalassembly.wistia.com/medias/f894zqb0dm?embedType=async&videoFoam=true&videoWidth=640)

--------------------------------

_Slide Title_: Lesson Practice

_Slide Content_:

Ready for some practice? Go to [repl.it/python](https://repl.it/languages/python) and try your hand at the following challenges. Repl.it is a safe online code editor that will allow you to practice the material you've learned here.

* For best results, don't move onto the next slide until you've tried every step!

## Open up [Repl.it](https://repl.it/languages/python) and give these a try:

1. Create an `int` called `my_int` and set it equal to `5`.
		
2. Add `4` to `my_int`.

3. Create a `float` called `my_float` and set it to `3.2`.

4. Create a `string` called `my_string` and set it to `'hello'`.

5. Create a `boolean` called `my_bool` and set it equal to `True`.

6. Add `my_bool` to `my_int`.

7. Add `my_bool` to `my_float`.

8. Change `my_bool` to `False` and add it to `my_float`.

9. Add `my_int` to `my_float`.

10. Add `my_int` to `my_string`. Does it work? If not, get it to work.


--------------------------------

_Slide Title_: Lesson Practice Solutions

_Slide Content_:

Have you finished practicing? Next, check your work against our suggested solutions below:

## Open up [Repl.it](https://repl.it/languages/python) and complete the following:

1. Create an `int` called `my_int` and set it equal to `5`.
		
		my_int = 5
2. Add `4` to `my_int`.

		my_int += 4
3. Create a `float` called `my_float` and set it to `3.2`.

		my_float = 3.2
4. Create a `string` called `my_string` and set it to `'hello'`.

		my_string = 'hello'
5. Create a `boolean` called `my_bool` and set it equal to `True`.

		my_bool = True
6. Add `my_bool` to `my_int`.

		print(my_bool+my_int)
7. Add `my_bool` to `my_float`.

		print(my_bool+my_float)
8. Change `my_bool` to `False` and add it to `my_float`.

		my_bool = False
		print(my_bool+my_float)

9. Add `my_int` to `my_float`.

		print(my_int+my_float)
10. Add `my_int` to `my_string`. Does it work? If not, get it to work.

		print(my_int+my_string)
		print(str(my_int)+my_string)

----------------------------------

_Slide Title_: Lesson Review

_Slide Content_:

_By now you should have a solid understanding of..._

+ Python's role in data science.
+ How to assign and manipulate variables.
+ Primitive Python data types and common use cases (e.g., int, float, str).
+ Basic string indexing and built-in methods.

**End-of-Lesson Quiz**

The following eight-question quiz is designed to help you assess your knowlege of the above criteria.

----------------------------------

_Description_: Select the best answer.

_Prompt*_:  Which of the following is untrue about Python?

_Choices:*_

1. Some Python modules, such as `numpy`, are partially written in C, allowing them to be fast and memory-efficient.
2. Python has many built-in data types, including Strings, Numbers, Tables, and Dictionaries. *
3. Many third-party modules exist, making it easy to utilize objects, functions, and classes others have created.
4. Python is interpreted and allows you to interactively evaluate code.

_Explanation*_: Tables are not a built-in data type. However, third-party libraries such as Pandas provide additional data types such as the `DataFrame`, which is similar to a table.

----------------------------------

_Description_: Select the best answer.

_Prompt*_: What does the following Python code evaluate to?

```
str(1 + 1)
```

_Choices:*_

1. `2`
2. `11`
3. `'2'` *
4. `'11'`
5. None of the above

_Explanation*_: First, `1 + 1` is evaluated to `2`, since both are integers. Next, the `str()` built-in function is called, converting the integer `2` to the string `'2'`.

----------------------------------

_Description_: Select the best answer.

_Prompt*_:  What are the data types of the following? `+42`, `1`, `False`, `float(False)`

_Choices:*_

1. `int`, `bool`, `bool`, `float`
2. `int`, `int`, `bool`, `bool`
3. `int`, `float`, `bool`, `bool`
4. `int`, `int`, `bool`, `float` *

_Explanation*_: The `float()` built-in function converts the value passed in to a `float`! Note that `1` by itself is an `int` (even though `True` is internally represented as `1`).

----------------------------------

_Description_: Select the best answer.

_Prompt*_: Suppose that `answer = 'Yes'`. What is stored in `is_correct` after this code is evaluated?

```
is_correct = (answer.lower() != "yes")
```

_Choices:*_

1. `"yes"`
2. `'True'`
3. `'False'`
4. `True`
5. `False` *

_Explanation*_: Note that three of the possible answers are string types. The comparison operators never evaluate to strings — only to booleans, `True` or `False`. So, these are the only valid answers. Let's walk through how the rest of the code is evaluated. First, `answer.lower()` evaluates to `'yes'`. Next, we see the operator `!=`. Because `'yes'` is the same as `'yes'`, they are not unequal — so the `!=` operator will evaluate to `False`. So, this statement becomes `is_correct = False` and `False` is assigned to the name `is_correct`. 

----------------------------------

_Description_: Select the best answer.


_Prompt*_:  What is the value of `title` after the following code is run?

```python
title = 'Data Science'
title = title + ' is awesome!'
```

_Choices:*_

1. `Data Science`
2. `Data Scienceis awesome!`
3. `Data Science is awesome!` *
4. `data science is awesome!`

_Explanation*_: Here, adding two strings concatenates them! Note there is a space in between the quote and `is`, so that will be contained in the final string.

----------------------------------

_Description_: Select the best answer.

_Prompt*_:  Every hour, I want my computer to run some Python code that scrapes a website. Which method would be the most practical way to run the code?

_Choices:*_

1. Manually run the code interactively in an `ipython` REPL.
2. Have the computer run a Python script. *
3. Save a Jupyter notebook then execute the notebook.

_Explanation*_: We would definitely not want to manually run the code every hour! Jupyter notebook files can possibly be run automatedly, but they contain a lot of extraneous information and are typically only used interactively. A script, however, is intended to be run independently.

> Note that it is very healthy to use a REPL or Jupyter notebook to experiment with scraping. However, the working code would ultimately be copied over to a script.

----------------------------------

_Description_: Select the best answer.

_Prompt*_:  Suppose you are writing a new function intended to load in data. [According to PEP 8](https://www.python.org/dev/peps/pep-0008/), which of the following function names would be most appropriate?

_Choices:*_

1. `loadData`
2. `load_data` *
3. `LoadData`
4. `LOAD_DATA`

_Explanation*_:  Both function names and variable names should be written `lower_case_with_underscores`. Constant variables (that never change value) are written `UPPER_CASE_WITH_UNDERSCORES`. Class names and type variable names are written `CamelCase`. In Python, we generally do not use `mixedCase`. **Pro tip:** After writing more Python code, PEP 8 will become more interesting!

----------------------------------

_Description_: Select the best answer.

_Prompt*_: Suppose `greeting = 'hi'`. Which of the following does not evaluate to `'Hi'`?

_Choices:*_
 
1. `greeting.upper()[0].lower() + greeting[1]` *
2. `greeting.upper()[0] + greeting[1].lower()`
3. `greeting[0].upper() + greeting[1]`
4. `greeting.capitalize()`
5. All of the above evaluate to `'Hi'`.

_Explanation*_: Recall that adding two strings concatenates them. Reading left to right, `greeting.upper()` evaluates to `'HI'`. So, `greeting.upper()[0]` indexes the first character which is `'H'`. Adding on a final `lower()`, `greeting.upper()[0].lower()` becomes `'h'`. So `'h' + greeting[1]` evaluates to `'hi'`, which is not `'Hi'`. From your exploration earlier of string methods, `capitalize()` is a built-in method that capitalizes only the first letter and lowercases everything else.

----------------------------------

_Slide Title_: Additional Resources

_Slide Content_:

If you're interested in gaining more practice with this topic, check out the following resource:

- [Datacamp: Intro to Python for Data Science](https://www.datacamp.com/courses/intro-to-python-for-data-science), Section 1: "Python Basics." Specifically, see the parts on "variable types" onwards.
- [Codecademy: Python](https://www.codecademy.com/learn/python), Section 5: "Lists and Dictionaries."
- [Datacamp: Intermediate Python for Data Science](https://www.datacamp.com/courses/intermediate-python-for-data-science), Section 2: "Dictionaries & Pandas." Specifically, see parts 1 and 2 on "Dictionaries."
