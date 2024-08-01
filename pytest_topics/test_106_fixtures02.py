import pytest
import os

weekdays1 = ['mon', 'tue', 'wed']
weekdays2 = ['fri', 'sat', 'sun']
filename = 'file1.txt'

# in the below function, before the yield statement whatever we write is the setup part, setting up connections etc...
# After the yield statement everything you see is a part of the teardown part, eg: close connections etc    
@pytest.fixture
def setup01():
    wk1 = weekdays1.copy()
    wk1.append('thur')
    print(f"printing wk1 from setup01 {wk1}") 
    yield wk1
    print("After yield in setup01 fixture")
    # wk1.clear()
    wk1.pop()
    print(f"After yield in setup01 fixture wk1 {wk1}")

def test_extendList(setup01):
    setup01.extend(weekdays2)
    assert setup01 == ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']

@pytest.fixture
def setup02():
    wk2 = weekdays2.copy()
    wk2.insert(0, 'thur')
    yield wk2

def test_len(setup01, setup02):
    print(len(weekdays1 + setup02) == len(setup01 + weekdays2))

@pytest.fixture
def setup03():
    f = open(filename, 'w')
    f.write("Pytest is good")
    f.close()
    f = open(filename, 'r+')
    yield f
    f.close()
    os.remove(filename)
    
 
def test_filetest(setup03):
    assert (setup03.readline()) == "Pytest is good"
    

    
    