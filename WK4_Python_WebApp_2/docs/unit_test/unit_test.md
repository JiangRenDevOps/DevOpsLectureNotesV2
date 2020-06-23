# What is unit test?

Unit testing is a type of testing to check if the small piece of code is doing what it is suppose to do.

# More details 
Unit testing involves breaking your program into pieces, and subjecting each piece to a series of tests.

Usually tests are run as separate programs, but the method of testing varies, depending on the language, and type of software (GUI, command-line, library).

Most languages have [unit testing frameworks](https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks), you should look into one for yours.

Tests are usually run periodically, often after every change to the source code. The more often the better, because the sooner you will catch problems.

# What frameworks are available to Python?

* unittest
* pytest
* nosetest

# Key concepts

### test fixture
A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. 
This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

### test case
A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. 
unittest provides a base class, TestCase, which may be used to create new test cases.

### test suite
A test suite is a collection of test cases, test suites, or both. 
It is used to aggregate tests that should be executed together.

### test runner
A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. 
The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.


# Hands on 

Let us do a simple comparison with the three framework

### Installation
```
pip3 install nosetests
pip3 install pytests
```

### Run the following
```
cd hands_on
```
#### unittest
```
python -m unittest -v
```
`-m` means module

`-v` means verbose

#### nose

```
nosetests -v
```

#### pytest

```
pytest
```
What do you observe?


### Rerun for EasyCRM
open EasyCRM directory and run the above commands again


# More to Read

http://www.rohitschauhan.com/index.php/2018/07/05/python-relative-benefits-of-pytest-unittest-nose-and-doctest

