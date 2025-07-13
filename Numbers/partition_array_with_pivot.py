def pivotArray(nums, pivot):
    less = []
    equal = []
    greater = []

    for num in nums:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)

    less.extend(equal)
    less.extend(greater)

    return less


nums = [9, 12, 3, 5, 14, 10, 10]
pivot = 10

print(pivotArray(nums,pivot))