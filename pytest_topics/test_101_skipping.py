import pytest
import sys

# Giving the following flag will skip this entire test file if the condition is met.
pytestmark = pytest.mark.skipif(sys.platform != "linux", reason = "Will run only on linux")

const = 9/5

def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah
    
# print(cent_to_fah())

def test_case01():
    assert type(const) == float

def test_case02():
    assert cent_to_fah() == 32
    
def test_case03():
    assert cent_to_fah(38) == 100.4
    
# the following decorator can be used to skip a test.
@pytest.mark.skip()
def test_case04():
    assert cent_to_fah(38) == 100.4
    

# the following decorator can be used to skip a test.
@pytest.mark.skip(reason = "Skipping for no reason specified")
def test_case05():
    assert cent_to_fah(38) == 100.4
    
# the following decorator can be used to skip a test.
@pytest.mark.skipif(sys.version_info > (3,6), reason = "dosen't work on python version above 3.6")
def test_case06():
    assert cent_to_fah(38) == 100.4
    
# the following decorator can be used to skip a test.
@pytest.mark.skipif(cent_to_fah() == 32, reason = "default value test so skipping")
def test_case07():
    assert cent_to_fah() == 32
    
    
# the following decorator can be used to skip a test.
@pytest.mark.skipif(pytest.__version__ < '8.2.2', reason = "pytest version below 8.2.2")
def test_case08():
    assert cent_to_fah() == 32
    
    
    
    