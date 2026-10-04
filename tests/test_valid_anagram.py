import pytest

from arrays_and_hashmaps.valid_anagram import valid_anagram


@pytest.mark.parametrize(
    ("s1", "s2", "expected"),
    [
        ("anagram", "nagaram", True),
        ("listen", "silent", True),
        ("rat", "car", False),
        ("aacc", "ccac", False),  # Same length, different character counts
        ("a", "", False),
        ("", "", True),
    ],
)
def test_valid_anagram(s1, s2, expected):
    assert valid_anagram(s1, s2) is expected