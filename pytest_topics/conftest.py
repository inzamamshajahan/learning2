import pytest

def pytest_configure():
    pytest.weekdays1 = ['mon', 'tue', 'wed']
    pytest.weekdays2 = ['fri','sat', 'sun']
    
# scope = module means that it is having module scope, by default its F, which means function scope
@pytest.fixture(scope = 'module') 
def setup01():
    wk = pytest.weekdays1.copy()
    wk.append('thur')
    yield wk
    print("\n Fixture setup01 closing")
    # wk1.clear()
    wk.pop()
    
@pytest.fixture()
def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, 'thur')
    yield wk2
    
@pytest.fixture()
def setup04(request):
    print(f"In fixture setup04")
    print(f"\n Fixture Scope: {request.scope}")
    print(f"\n Calling Function: {str(request.function.__name__)}")
    print(f"\n Calling Module: {str(request.module.__name__)}")
    
    