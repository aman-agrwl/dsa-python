import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from arrays_and_hashmaps.valid_anagram import valid_anagram


test_cases = [
    ("anagram", "nagaram", True, "Anagrams with repeated characters"),
    ("listen", "silent", True, "Anagrams with distinct characters"),
    ("rat", "car", False, "Different characters"),
    ("aacc", "ccac", False, "Different character frequencies"),
    ("a", "", False, "Strings of different lengths"),
    ("", "", True, "Both strings empty"),
]


if __name__ == "__main__":
    for s1, s2, expected, description in test_cases:
        result = valid_anagram(s1, s2)
        assert result is expected, (
            f"Failed: {description} | Got {result}, expected {expected}"
        )
        print(f"Passed: {description}")