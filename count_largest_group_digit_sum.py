def countLargestGroup(n: int):
    mpp = {}
    maxi, count = 0, 0

    for i in range(1, n + 1):
        x = digsum(i)
        mpp[x] = mpp.get(x, 0) + 1
        maxi = max(maxi, mpp[x])

    for v in mpp.values():
        if v == maxi:
            count += 1
    return count


def digsum(n):
    s = str(n)
    sum = 0
    for ch in s: sum += int(ch)
    return sum


# Example usage
# N = 15
# [1,10] [2,11] [3,12] [4,13] [5,14] [6,15] [7] [8] [9]
# Output: 6
# 1,10 => 1, 1+0=1 /// 2,11 => 2, 1+1=2

print(countLargestGroup(15))  # 6
print(countLargestGroup(50)) # 1
print(countLargestGroup(25)) # 6