def summation(num):
    pass  # Code here

    n = num
    res = 0

    for idx in range(0, n):
        res += (n - idx)

    return res


def summation2(num):
    return sum(range(1,num+1))


# Test cases
print(summation(1), summation2(1), "should be 1")
print(summation(2), summation2(2), "should be 3")
print(summation(8), summation2(8), "should be 36")
print(summation(10), summation2(10), "should be 55")
print(summation(15), summation2(15), "should be 120")
print(summation(18), summation2(18), "should be 171")
print(summation(25), summation2(25), "should be 325")