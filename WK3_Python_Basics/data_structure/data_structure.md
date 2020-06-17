# [Abstract Data Type and Data Structures](https://www.datacamp.com/community/tutorials/data-structures-python#adt)

As you read in the introduction, data structures help you to focus on the bigger picture rather than getting lost in the details. This is known as data abstraction.

Now, data structures are actually an implementation of Abstract Data Types or ADT. This implementation requires a physical view of data using some collection of programming constructs and basic data types.

Generally, data structures can be divided into two categories in computer science: primitive and non-primitive data structures. The former are the simplest forms of representing data, whereas the latter are more advanced: they contain the primitive data structures within more complex data structures for special purposes.

# Real world questions

In each of the following examples, please choose the best data structure(s).
Options are: Array, Linked Lists, Stack, Queues, Trees, Graphs, Sets, Hash
Tables. Note that there may not be one clear answer.
1. You have to store social network “feeds”. You do not know the size, and
things may need to be dynamically added.
2. You need to store undo/redo operations in a word processor.
3. You need to evaluate an expression (i.e., parse).
4. You need to store the friendship information on a social networking site.
I.e., who is friends with who.
5. You need to store an image (1000 by 1000 pixels) as a bitmap.
6. To implement printer spooler so that jobs can be printed in the order of
their arrival.
7. To implement back functionality in the internet browser.
8. To store the possible moves in a chess game.
9. To store a set of fixed key words which are referenced very frequently.
10. To store the customer order information in a drive-in burger place. (Customers keep on coming and they have to get their correct food at the
payment/food collection window.)
11. To store the genealogy information of biological species.
12. You need to implement a auto retrieval/suggestion in a search query with a subset of the characters
13. You need to prioritise the video traffic that goes into the router

# Why DevOps should care?

We do automation and we need to know what is our best available choices are?

Are there any existing methods/libraries/data structure that can help us achieve the task?

Sometimes hotfix may require us writing scripts to fetch data, process certain tasks and send the results out

# Primitive Data Structures

* Integers
* Float
* Strings
* Boolean

## Integers

You can use an integer represent numeric data, and more specifically, whole numbers from negative infinity to infinity, like 4, 5, or -1.

## Float

"Float" stands for 'floating point number'. You can use it for rational numbers, usually ending with a decimal figure, such as 1.11 or 3.14.

```
# Floats
x = 4.0
y = 3.0

# Addition
print(x + y)

# Subtraction
print(x - y)

# Multiplication
print(x * y)

# Returns the quotient
print(x / y)

# Returns the remainder
print(x % y) 

# Absolute value
print(abs(x))

# x to the power y
print(x ** y)
```

What if you change x to 4 and y to 3?

You can use `type` to validate the returned type

```
print(type(x/y))
```

# Strings

Strings are collections of alphabets, words or other characters. In Python, you can create strings by enclosing a sequence of characters within a pair of single or double quotes. For example: 'cake', "cookie", etc.

```
x = 'Cake'
y = 'Cookie'
print(x + ' & ' + y)
```
output:
```
Cake Cookie
```

## Boolean

This built-in data type that can take up the values: True and False, which often makes them interchangeable with the integers 1 and 0. 
Booleans are useful in conditional and comparison expressions, just like in the following examples:

```
x = 4
y = 2
print(x == y)

z = (x==y)     # Comparison expression (Evaluates to false)
if z:          # Conditional on truth/false value of 'z'
    print("Cookie")
else: 
    print("No Cookie")
```

# Non-Primitive Data Structures

* Arrays
* Lists
* Tuples
* Dictionary
* Sets
* Files

## Arrays

First off, arrays in Python are a compact way of collecting basic data types, all the entries in an array must be of the same data type.

```
arrayIdentifierName = array(typecode, [Initializers])
```

```
‘b’ -> Represents signed integer of size 1 byte
‘B’ -> Represents unsigned integer of size 1 byte
‘c’ -> Represents character of size 1 byte
‘u’ -> Represents unicode character of size 2 bytes
‘h’ -> Represents signed integer of size 2 bytes
‘H’ -> Represents unsigned integer of size 2 bytes
‘i’ -> Represents signed integer of size 2 bytes
‘I’ -> Represents unsigned integer of size 2 bytes
‘w’ -> Represents unicode character of size 4 bytes
‘l’ -> Represents signed integer of size 4 bytes
‘L’ -> Represents unsigned integer of size 4 bytes
‘f’ -> Represents floating point of size 4 bytes
‘d’ -> Represents floating point of size 8 bytes
```

For you to read: https://www.thoughtco.com/definition-of-unsigned-958174
Question: what would be the largest unsigned integer that your laptop can present?

```
arr = array('I', [3, 6, 9])
for elem in arr:
    print(elem)
```

Array is more efficient and apply certain functions to all the elements easily, since they have the same type

```
array_char = array.array("u",["c","a","t","s"])
array_char.tostring()
print(array_char)
```

### Numpy Array

It is also worthwhile to mention the NumPy array while we are on the topic of arrays. 

NumPy arrays are very heavily used in the data science world to work with multidimensional arrays.
 
They are more efficient than the array module and Python lists in general. 

Reading and writing elements in a NumPy array is faster, and they support "vectorized" operations such as elementwise addition. 

Also, NumPy arrays work efficiently with large sparse datasets. 

To learn more, check out DataCamp's [Python Numpy Array Tutorial](https://www.datacamp.com/community/tutorials/python-numpy-tutorial).

```
multi_arr_ones = np.ones((3,4)) # Creating 2D array with 3 rows and 4 columns
print(multi_arr_ones)
```

Output:
```
[[ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]]
```


## Lists

Lists in Python are used to store collection of heterogeneous items. 

These are mutable, which means that you can change their content without changing their identity. 

You can recognize lists by their square brackets `[` and `]` that hold elements, separated by a comma `,`. 

Lists are built into Python: you do not need to invoke them separately.

see `data_structure.py` for practice

### Stacks

A stack is a container of objects that are inserted and removed according to the Last-In-First-Out (LIFO) concept. 

Think of a scenario where at a dinner party where there is a stack of plates, plates are always added or removed from the top of the pile. 

In computer science, this concept is used for evaluating expressions and syntax parsing, scheduling algortihms/routines, etc.

```
# Bottom -> 1 -> 2 -> 3 -> 4 -> 5 (Top)
stack = [1,2,3,4,5] 
stack.append(6) # Bottom -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 (Top)
print(stack)
```
```
[1, 2, 3, 4, 5, 6]
```
```
stack.pop() # Bottom -> 1 -> 2 -> 3 -> 4 -> 5 (Top)
stack.pop() # Bottom -> 1 -> 2 -> 3 -> 4 (Top)
print(stack)
```
```
[1, 2, 3, 4]
```

#### Real world examples 

To reverse a word. You push a given word to stack - letter by letter - and then pop letters from the stack.

An "undo" mechanism in text editors; this operation is accomplished by keeping all text changes in a stack.
 * Undo/Redo stacks in Excel or Word.

* Language processing :
    * space for parameters and local variables is created internally using a stack.

    * compiler's syntax check for matching braces is implemented by using stack.

* A stack of plates/books in a cupboard.

* A garage that is only one car wide. To remove the first car in we have to take out all the other cars in after it.

* Wearing/Removing Bangles.

* Back/Forward stacks on browsers.
* Support for recursion

* Activation records of method calls.

### Queues

A queue is a container of objects that are inserted and removed according to the First-In-First-Out (FIFO) principle. 

An excellent example of a queue in the real world is the line at a ticket counter where people are catered according to their arrival sequence and hence the person who arrives first is also the first to leave. 

Queues can be of many different kinds.

Lists are not efficient to implement a queue, because `append()` and `pop()` from the end of a list is not fast and incur a memory movement cost. 

Also, insertion at the end and deletion from the beginning of a list is not so fast since it requires a shift in the element positions.

[Hands-on] Could you write a simple Queue using List?


## Tuples

Keywords: Immutable

Tuples are another standard sequence data type. 

The difference between tuples and list is that tuples are immutable, which means once defined you cannot delete, add or edit any values inside it. 

This might be useful in situations where you might to pass the control to someone else but you do not want them to manipulate data in your collection, but rather maybe just see them or perform operations separately in a copy of the data.

see `data_structure.py` for practice

## Dictionary

Keywords: Key/Value Pair; Save Time with Space

Dictionaries are exactly what you need if you want to implement something similar to a telephone book. None of the data structures that you have seen before are suitable for a telephone book.
   
This is when a dictionary can come in handy. Dictionaries are made up of key-value pairs. 

key is used to identify the item and the value holds as the name suggests, the value of the item.

```
x_dict = {'Edward':1, 'Jorge':2, 'Prem':3, 'Joe':4}
print(x_dict[Joe])
```
```
4
```

## Sets

Keywords: Distinct/Unique

Sets are a collection of distinct (unique) objects. 

These are useful to create lists that only hold unique values in the dataset. 

It is an unordered collection but a mutable one, this is very helpful when going through a huge dataset.

```
x_set = set('CAKE&COKE')
y_set = set('COOKIE')

print(x_set)
```
```
{'A', '&', 'O', 'E', 'C', 'K'}
```
please try the following operations
```
print(x_set - y_set) # All the elements in x_set but not in y_set
print(x_set|y_set) # Unique elements in x_set or y_set or both
print(x_set & y_set) # Elements in both x_set and y_set
```

# Files 

At its core, a file is a contiguous set of bytes used to store data. This data is organized in a specific format and can be anything as simple as a text file or as complicated as a program executable. In the end, these byte files are then translated into binary 1 and 0 for easier processing by the computer.

Files on most modern file systems are composed of three main parts:

* Header: metadata about the contents of the file (file name, size, type, and so on)
* Data: contents of the file as written by the creator or editor
* End of file (EOF): special character that indicates the end of the file

## File Paths

When you access a file on an operating system, a file path is required. The file path is a string that represents the location of a file. It’s broken up into three major parts:

* Folder Path: the file folder location on the file system where subsequent folders are separated by a forward slash / (Unix) or backslash \ (Windows)
* File Name: the actual name of the file
* Extension: the end of the file path pre-pended with a period (.) used to indicate the file type

```
/
│
├── parent_folder/
|   │
│   ├── gif_folder/
│   │   └── cats.gif
│   │
│   └── dog_breeds.txt
|
└── animals.csv
```

## Line Endings

* ISO standard
* Carriage return means to return to the beginning of the current line without advancing downward. The name comes from a printer's carriage, as monitors were rare when the name was coined. This is commonly escaped as \r, abbreviated CR, and has ASCII value 13 or 0x0D.
* Linefeed means to advance downward to the next line; however, it has been repurposed and renamed. Used as "newline", it terminates lines (commonly confused with separating lines). This is commonly escaped as \n, abbreviated LF or NL, and has ASCII value 10 or 0x0A. CRLF (but not CRNL) is used for the pair \r\n.

Try the following example and see if you understand what they do:
```
print("abc")
print("abc\n")
print("abc\rdef\n")
print("abcxyz\rdef\n")
print("abc", end="")
```



# Advanced Data Structure

## Linear data structures (Basics)

* Stacks
* Queues

## Non-Linear data structures (Advanced)

* Graphs
    * how to present the data?
        * dict + set
            * see `graph.py` for understanding
        * numpy
    * how to find the shortest path
        * BFS/DFS
            * dijkstra's algorithm
            
* Trees
    * binary tree (divide and conquer)
    * heap tree (priority queue)
    * trie (search engine suggestions)
        * see `data_structure.py` for practice
    
https://realpython.com/python-data-types/

