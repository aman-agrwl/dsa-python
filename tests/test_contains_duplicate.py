import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from arrays_and_hashmaps.contains_duplicate import contains_duplicate


# Each tuple contains: (nums, target, expected_output, test_description)
test_cases = [
    ([1,2,3,1], True,  "Duplicate exists at start and end"),
    ([1, 2, 3, 4], False, "All elememts are unique"),
   ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True, "Multiple duplicates"),
    ([], False, "Empty array"),
    ([5], False, "Single element array"),
]


def test_contains_duplicate_cases():
    for nums, expected, description in test_cases:
        result = contains_duplicate(nums)

        # Validate output against expected result
        assert result == expected, f"Failed: '{description}' | Got {result}, expected {expected}"
        print(f"Passed: {description}")


if __name__ == "__main__":
    test_contains_duplicate_cases()