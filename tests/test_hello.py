from lib.hello import *
import pytest

def test_hello_takes_a_name_and_says_hello_name():
    actual = hello('Jordan')

    expected = 'Hello Jordan, how are you today?'

    assert actual == expected

def test_hello_raises_error_when_not_string_passed_in():
    with pytest.raises(Exception) as err:
        say_hello = hello(13)
    
    actual = str(err.value)
    
    expected = 'You can only pass strings into hello() function'

    assert actual == expected