def maximumCount(nums):
    count_pos = 0
    count_neg = 0

    for num in nums:
        if num > 0:
            count_pos += 1
        if num < 0:
            count_neg += 1
    return max(count_pos, count_neg)



nums1=[-2,-1,-1,1,2,3]
nums2=[5,20,66,1314]
nums3=[-5,20,100]
nums4=[-20,-10,-5,-3,-1,0,0,1,2,5,10]

print(maximumCount(nums1)) # 3 both
print(maximumCount(nums2)) # 4 pos
print(maximumCount(nums3)) # 2 pos
print(maximumCount(nums4)) # 5 neg