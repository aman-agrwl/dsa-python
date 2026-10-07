import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from arrays_and_hashmaps.first_missing_positive import first_missing_pos


test_cases = [
    ([1, 2, 0], 3, "Missing value after a sequence"),
    ([2, 1], 3, "Consecutive values in unsorted order"),
    ([3, 4, -1, 1], 2, "Mixed positive and negative values"),
    ([7, 8, 9, 11, 12], 1, "Smallest positive value is missing"),
    ([], 1, "Empty array"),
    ([1], 2, "Single value starts at one"),
    ([2], 1, "Single value does not start at one"),
    ([1, 1], 2, "Duplicate values"),
    ([1, 2, 3], 4, "Consecutive values from one"),
    ([-3, -2, -1], 1, "Only negative values"),
]


if __name__ == "__main__":
    for nums, expected, description in test_cases:
        result = first_missing_pos(nums)
        assert result == expected, (
            f"Failed: {description} | Got {result}, expected {expected}"
        )
        print(f"Passed: {description}")
