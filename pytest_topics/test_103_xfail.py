# x fail is used when we expect a test to fail, for some reason eg: known bug
import pytest
import sys


# The below test will pass.
def test_strjoin():
    s1 = 'Python,Pytest and Automation'
    l1 = ['Python,Pytest', 'and', 'Automation']
    l2 = ['Python', 'Pytest and Automation']
    assert ' '.join(l1) == s1

# below test will XPASS, since we are expecting it to fail but it is actually passing    
@pytest.mark.xfail(reason = "testing xfail feature")
def test_strjoin1():
    s1 = 'Python,Pytest and Automation'
    l1 = ['Python,Pytest', 'and', 'Automation']
    l2 = ['Python', 'Pytest and Automation']
    assert ' '.join(l1) == s1

# the below test says that this test is expecting an index error, therefore if it gives an index error it will pass xfail.
@pytest.mark.xfail(raises=IndexError, reason="known issue")
def test_str04():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[100]
    
# the below test says that this test is expecting an index error, therefore if it does not give an index error it will pass xpass.
@pytest.mark.xfail(raises=IndexError, reason="known issue")
def test_str04_1():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[10]
    
# the below test says that this test is expecting a TypeError, therefore if it gives an index error it will fail. (FAILED)
@pytest.mark.xfail(raises=TypeError, reason="known issue2")
def test_str04_2():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[100]

# below test failed, as i was running it from a linux machine, therefore it was expecting the platform to be win32 (FAILED)
@pytest.mark.xfail(sys.platform=='win32', reason="works only in win32")
def test_str05():
    letters = 'abcd'
    num = 1234
    assert letters + num == 'abcd1234'

# below test XFAILED, as i was running the test from a linux machine, here the expectation was to fail and it failed. (XFAIL)
@pytest.mark.xfail(sys.platform=='linux', reason="works only in linux")
def test_str06():
    letters = 'abcd'
    num = 1234
    assert letters + num == 'abcd1234'
    
"""
Below is a section of the output: 

pytest_topics/test_103_xfail.py::test_strjoin PASSED                                                                             [ 14%]
pytest_topics/test_103_xfail.py::test_strjoin1 XPASS (testing xfail feature)                                                     [ 28%]
pytest_topics/test_103_xfail.py::test_str04 XFAIL (known issue)                                                                  [ 42%]
pytest_topics/test_103_xfail.py::test_str04_1 XPASS (known issue)                                                                [ 57%]
pytest_topics/test_103_xfail.py::test_str04_2 FAILED                                                                             [ 71%]
pytest_topics/test_103_xfail.py::test_str05 FAILED                                                                               [ 85%]
pytest_topics/test_103_xfail.py::test_str06 XFAIL (works only in linux)                                                          [100%]

"""