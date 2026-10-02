# Problem Statement
# Given an integer array nums, return True if any value appears at least twice in the array, and return False if every element is distinct.

# Example 1:
# Input: nums = [1, 2, 3, 1]

# Output: True (because 1 appears twice)

# Example 2:
# Input: nums = [1, 2, 3, 4]

# Output: False (all elements are unique)


def contains_duplicate(nums: list[int])-> bool:
	seen = {}
	for num in nums:
		if num in seen:
			return True
		seen[num] = True
	return False

if __name__ == "__main__":
    numbers = [1,2,3,1,4]
    print(contains_duplicate(numbers))

