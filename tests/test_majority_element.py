import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from arrays_and_hashmaps.majority_element import majority_elem

test_cases = [
    ([3, 2, 3], 3, "Majority appears at both ends"),
    ([2, 2, 1, 1, 1, 2, 2], 2, "Majority appears throughout"),
    ([1], 1, "Single-element array"),
    ([1, 1, 2], 1, "Majority appears first"),
    ([-1, -1, 2], -1, "Negative majority element"),
]


if __name__ == "__main__":
    for nums, expected, description in test_cases:
        result = majority_elem(nums)
        assert result == expected, (
            f"Failed: {description} | Got {result}, expected {expected}"
        )
        print(f"Passed: {description}")
