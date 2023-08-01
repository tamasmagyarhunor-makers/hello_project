from lib.hello import *

def test_hello_takes_a_name_and_says_hello_name():
    actual = hello('Jordan')

    expected = 'Hello Jordan, how are you today?'

    assert actual == expected