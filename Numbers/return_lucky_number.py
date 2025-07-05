from collections import Counter


def findLucky(nums) -> int:
    freq = Counter(nums)
    lucky = -1
    for num, count in freq.items():
        if num == count:
            lucky = max(lucky, num)
    return lucky


# Example usage:
print(findLucky([2, 2, 3, 4]))  # Output: -1
print(findLucky([1, 2, 2, 3, 3, 3]))  # Output: 3
print(findLucky([2, 2, 3, 4, 4, 4, 4]))  # Output: 4
