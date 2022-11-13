import pytest1 # remember pytest1 is our file name.
import pytest

def test_add():
    # REmember pytest1 is our python file name
    assert pytest1.add(4,5)==9
def test_sub():
    assert pytest1.sub(4,5)==-1