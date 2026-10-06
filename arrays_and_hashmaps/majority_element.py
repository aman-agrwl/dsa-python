"""
Problem: Majority Element

Given an integer array nums, return the element that appears more than
floor(len(nums) / 2) times. You may assume a majority element exists.

Examples:
    [3, 2, 3] -> 3
    [2, 2, 1, 1, 1, 2, 2] -> 2
"""


def majority_elem(nums: list[int]) -> int:
    
    state = {}
    
    for num in nums:
        state[num] = state.get(num, 0) + 1
        if(state[num] > len(nums)//2):
            return num
        

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
