# Markeres are used to group the tests
# we will be able to run just the marked tests as a group using -m option
# Eg: pytest -v -m sanity pytest_topics/test_102_markers.py
# Eg: pytest -v -m "sanity and str" pytest_topics/test_102_markers.py   (this will run only the tests with both the markers persent)

import pytest
pytestmark = [pytest.mark.smoke, pytest.mark.strtest]
# the above line is the pytest mark for the entire page
# so when we do pytest -v -m "smoke", only this file will be run 
# the command in the previous comment will run all the tests defined in this file, since for by using the pytestmark variable we are marking the entire file as smoke

@pytest.mark.sanity
def test_str01():
    num = 9/4
    s1 = 'I like ' + 'pytest automation'
    assert str(num) == '2.25'
    assert s1 == 'I like pytest automation'
    assert s1 + str(num) == 'I like pytest automation2.25'

@pytest.mark.sanity
def test_str02():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert len(letters) == 26

def test_str03():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[0] == 'a'
    assert letters[-1] == 'z' == letters[25]

@pytest.mark.sanity
@pytest.mark.str
def test_strslice():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[:] == letters
    assert letters[10:] == 'klmnopqrstuvwxyz'
    assert letters[-3:] == 'xyz'
    assert letters[:21:5] == 'afkpu'

@pytest.mark.str
def test_strsplit():
    s1 = 'Python,Pytest and Automation'
    assert s1.split() == ['Python,Pytest', 'and', 'Automation']
    assert s1.split(',') == ['Python', 'Pytest and Automation']

# tasks TBD
def test_strjoin():
    pass
    s1 = 'Python,Pytest and Automation'
    l1 = ['Python,Pytest', 'and', 'Automation']
    l2 = ['Python', 'Pytest and Automation']
