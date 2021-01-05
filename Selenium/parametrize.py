def test_is_palindrome_empty_string():
    assert is_palindrome("")

def test_is_palindrome_single_character():
    assert is_palindrome("a")

def test_is_palindrome_mixed_casing():
    assert is_palindrome("Bob")

def test_is_palindrome_with_spaces():
    assert is_palindrome("Never odd or even")

def test_is_palindrome_with_punctuation():
    assert is_palindrome("Do geese see God?")

def test_is_palindrome_not_palindrome():
    assert not is_palindrome("abc")

def test_is_palindrome_not_quite():
    assert not is_palindrome("abab")
    
"""
def test_is_palindrome_<in some situation>():
    assert is_palindrome("<some string>")
"""
import pytest

@pytest.mark.parameterize("palindrome", [
    # need either tuple or single values
    "",
    "a",
    "Bob",
    "Never odd or even",
    "Do geese see God?
])

def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome) == expected_result
    

@pytest.mark.parametrize("non_palindrome", [
    "abc",
    "abcb"
])
def test_is_palindrome_not_palindrome(non_palindrome):
    assert not is_palindrome(non_palindrome)



"""
We can combine the case even further here
"""

# comma separated value here
@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", True),
    ("Never odd or even", True),
    ("Do geese see God?", True)
    ("abc", False),
    ("abab", False),
])

def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result


