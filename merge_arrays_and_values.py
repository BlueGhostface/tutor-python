def mergeArrays(nums1,nums2):
    key_to_sum = {}

    # Copying the array nums1 to the map.
    for nums in nums1:
        key_to_sum[nums[0]] = nums[1]

    # Adding the values to existing keys or create new entries.
    for nums in nums2:
        key_to_sum[nums[0]] = key_to_sum.get(nums[0], 0) + nums[1]

    merged_array = []
    for key, value in sorted(key_to_sum.items()):
        merged_array.append([key, value])

    return merged_array

arr1= [[1,2],[2,3],[4,5]]
arr2= [[1,4],[3,2],[4,1], [5,7]]


print(mergeArrays(arr1, arr2))  # [[1, 6], [2, 3], [3, 2], [4, 6], [5, 7]]
