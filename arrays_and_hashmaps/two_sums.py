def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i

    return []


def two_sum_naive(nums, target):
    return two_sum(nums, target)


# Example usage
if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(two_sum(numbers, target))



