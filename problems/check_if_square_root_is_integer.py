import math

def is_square(n):
    if n >=0:
        root = math.sqrt(n)
        return root.is_integer()
    return False




def is_square2(n):
    return n > -1 and math.sqrt(n) % 1 == 0



print(is_square(-1),is_square2(-1), "false")
print(is_square(0), is_square2(0),"true")
print(is_square(3),is_square2(3),"false")
print(is_square(4),is_square2(4),"true")
print(is_square(9),is_square2(9),"true")
print(is_square(16),is_square2(16),"true")
print(is_square(25),is_square2(25),"true")

print(is_square(30),is_square2(30),"false")
print(is_square(48),is_square2(48),"false")
print(is_square(81),is_square2(81),"true")
print(is_square(100),is_square2(100),"true")
print(is_square(105),is_square2(105),"false")
