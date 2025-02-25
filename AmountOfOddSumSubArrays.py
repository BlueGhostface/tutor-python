from typing import List

# Given an array of integers arr. Return the number of sub-arrays with odd sum.
# example 1: arr = [1, 3, 5] All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
# All sub-arrays sum are [1,4,9,3,8,5].
# Odd sums are [1,9,3,5] so the answer is 4.

def numOfSubarrays(arr: List[int]) -> int:

    mod = 1e9 + 7 # constraint since the answer can be large
    n = len(arr)
    count =0

    for index in range(n):
        cursum = 0
        for curindex in range(index, n): # iterate through the array from a start position to make sub arrays
            cursum += arr[curindex]
            if cursum % 2 != 0: # if the sum is odd
                count += 1

    return int(count % mod)



print(numOfSubarrays([1, 3, 5]))  # 4
print(numOfSubarrays([2,4,6]))  # 0
print(numOfSubarrays([1,2,3,4,5,6,7]))  # 16