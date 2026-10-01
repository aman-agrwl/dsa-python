from arrays_and_hashmaps.two_sums import two_sum


# Each tuple contains: (nums, target, expected_output, test_description)
test_cases = [
    ([2, 7, 11, 15], 9, [0, 1], "Basic case with a valid pair at the beginning"),
    ([1, 2, 3, 4], 10, [], "No matching pair sums to target"),
    ([3, 3], 6, [0, 1], "Duplicate numbers adding up to target"),
    ([3, 2, 4], 6, [1, 2], "Pair located in the middle/end"),
    ([-1, -8, 0, 5], -9, [0, 1], "Negative numbers in array"),
]



def test_two_sum_cases():
    for nums, target, expected, description in test_cases:
        result = two_sum(nums, target)

        # Validate output against expected result
        assert result == expected, (
            f"Failed: '{description}' | Got {result}, expected {expected}"
        )

        print(f"✓ Passed: {description}")
