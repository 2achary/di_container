import pytest
from unittest.mock import patch, MagicMock
from using_di import TestThis


def r():
    return MagicMock()

@patch('using_di.di_container', return_value=r)
def test_my_class(my_patch):
    t = TestThis()
    t.myfunc.return_value = 'something'
    print(t.foo())


