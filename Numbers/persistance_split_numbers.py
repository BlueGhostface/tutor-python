# you need to keep multiplying the single digits of a number until you only have a single digit number left.
# and return the number of times you had to multiply the single digits to get to that single digit number
# 51 = 5*1 = 5 counter = 1
testnum1 = 51
testnum2 = 372
testnum3 = 6247

counter = 0

def persistence(n):
    nums = n
    counter = 0

    while len(str(nums)) > 1:
        intList = [ int(i) for i in list(str(nums))]

        result = 1
        for value in intList:
            result = result * value
        nums = result
        # print(nums)
        counter += 1

    return counter



print(persistence(testnum1))
print(persistence(testnum2))
print(persistence(testnum3))
