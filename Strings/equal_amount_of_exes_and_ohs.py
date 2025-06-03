def xo(s):
    count = 0
    s = s.lower()
    n = len(s)
    for idx in range(0, n):
        if s[idx] == 'x':
            count += 1
        if s[idx] == 'o':
            count -= 1

    if count == 0:
        return True
    else:
        return False





def xo2(s):
    s = s.lower()
    return s.count('x') == s.count('o')



teststr="xoxoxo"
teststr2="xoxox"
teststr3="xoxxoo"
teststr4="pspspsp"
teststr5="xxxooo"
teststr6="XXXOOOpsps"
teststr7="XXXOOoopsps"


print(xo(teststr), xo2(teststr),"should be True")
print(xo(teststr2), xo2(teststr2),"should be False")
print(xo(teststr3), xo2(teststr3),"should be True")
print(xo(teststr4), xo2(teststr4),"should be True")
print(xo(teststr5), xo2(teststr5),"should be True")
print(xo(teststr6), xo2(teststr6),"should be True")
print(xo(teststr7), xo2(teststr7),"should be False")