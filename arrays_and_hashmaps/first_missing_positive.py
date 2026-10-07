"""
Problem: First Missing Positive

Given an unsorted integer array nums, return the smallest positive integer
(greater than zero) that does not appear in nums. Your solution must run in
O(n) time and use O(1) extra space.

Examples:
    [1, 2, 0] -> 3
    [3, 4, -1, 1] -> 2
    [7, 8, 9, 11, 12] -> 1
"""


def first_missing_pos(nums: list[int]) -> int:
	missing_num = 1
	size = len(nums)
	index = 0
	
	while index < size:
		value = nums[index]
		target_index = value-1
		if 1<= value <= size and nums[target_index] != value:
			nums[index], nums[target_index] = nums[target_index], nums[index]
		else:
			index+=1
   
	for index, value in enumerate(nums):
		if value != index+1:
			return index+1
 
	return size+1
			
			
   
    
      
      
if __name__ == "__main__":
    numbers = [2, 3, 5, 1, 8]
    print(first_missing_pos(numbers))