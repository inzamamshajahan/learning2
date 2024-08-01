def test_a1(): # will pass
    assert 4 != 5
    
def test_a2(): # will pass
    assert 1
    
def test_a3(): # will pass
    assert 'abcd' == "abcd"
    
# below test will pass and also print the message
def test_a4(): 
    print("This is my first test")
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1

# the below test will fail.
# the first print statement will be printed if it fails, but the second print statement will not be printed.
def test_a5():
    print("This is my first test11")
    assert 9/5 == 1.5, "failed test intentionally"
    print("This is my first test22")

# the below test will pass
# if the test passes, none of the print statements will be shown in the terminal.
def test_a6():
    print("This is my first test11")
    assert 9/5 == 9/5, "passing test to see what all gets printed"
    print("This is my first test22")
    
# below test will pass    
def test_a7():
    assert 9//5 == 1

# below is an example of a class used for testing
# below test will pass
class TestMyStuff():
    def test_type(self):
        assert type(1) == int

import pytest

def test_case01(): # This test will pass
    with pytest.raises(Exception):
        assert(1/0)

def test_case02(): # This test will pass
    with pytest.raises(ZeroDivisionError):
        assert(1/0)
        
# This test will fail
# In this type of tests, if the assert statement do not raise the expected exception it will fail.
def test_case03(): 
    with pytest.raises(ZeroDivisionError):
        assert(1/1)

# This test will pass
# in this kind of test definition
"""
In Pytest, the pytest.raises assertion is used to check whether a specific exception is raised during the execution of a particular code block.

If the problem/exception occurs, the test passes; if not, the test fails.

In simpler terms, it's like saying, "I expect something to go wrong, and if it doesn't, then the test is not okay."

That's the essence of pytest.raises. It helps ensure that your code behaves as expected when certain issues arise.
"""

"""
QUESTION: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
he following code does not print the exception information:

def test_case02():
    with pytest.raises(Exception) as excinfo:
        assert (1, 2, 3) == (1, 2, 4)
 
    print(str(excinfo))
I ran it within Visual Studio Code / Test Explorer, the Visual Studio Code Python Debugger, and at the command line. All produced the following results:

================================= test session starts ==================================
platform darwin -- Python 3.10.7, pytest-7.1.3, pluggy-1.0.0
rootdir: /Volumes/ProjectsDrive/Continuing_Education/Automation-Testing-With-Pytest
collected 1 item                                                                            
 
py_assertions/test_module03.py .                                                 [100%]
 
================================ 1 passed in 0.00s =====================================

ANSWER: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Run pytest with option: -s

By default pytest captures standard-output while running tests. Only if a test fails, the captured output is shown.

Use this option for pytest to disable all capturing and print to stdout or to console.

E.g. pytest -s test_module03.py
"""

def test_case04():
    with pytest.raises(Exception) as excinfo:
        assert (1,2,3) == (1,2,4)
    print(excinfo)
    

"""
Below 2 funcions show how we can use to pytest to ensure that we are getting a particular error from a function.
"""

def func1():
    raise ValueError("IndexError func1 raised")
    
def test_case05():
    with pytest.raises(Exception) as excinfo:
        func1()
    print (str(excinfo))
    assert (str(excinfo.value)) == "IndexError func1 raised"




    
