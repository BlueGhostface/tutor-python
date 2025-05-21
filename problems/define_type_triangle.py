def triangleType(nums) -> str:
    nums.sort()
    if nums[0] + nums[1] <= nums[2]:
        return "none"
    elif nums[0] == nums[2]:
        return "equilateral"
    elif nums[0] == nums[1] or nums[1] == nums[2]:
        return "isosceles"
    else:
        return "scalene"


inputnums = [2, 2, 3]
inputnums2 = [3, 3, 3]
inputnums3 = [2, 1, 3]
inputnums4 = [3,4,5]

print(triangleType(inputnums))
print(triangleType(inputnums2))
print(triangleType(inputnums3))
print(triangleType(inputnums4))