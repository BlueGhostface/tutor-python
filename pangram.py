
testpangram = "The quick brown fox jumps over the lazy dog"
testnotpangram = "The quick brown cat jumps over the lazy cat"



def is_pangram(st):
    f=0
    if len(st) < 26:
        return False
    for char in st.lower():
        if char.isalpha() :
            f |= 1 << (ord(char) - ord('a'))

        if f == (1<<26 ) -1:
            return True
    return False


print(is_pangram(testpangram))
print(is_pangram(testnotpangram))