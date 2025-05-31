def duplicate_count(text):
    n=0
    text=text.lower()
    for i in set(text):
        if text.count(i) >1:
            n+=1
    return n

print(duplicate_count("abcde"), 0)
print(duplicate_count("aabbcde"), 2)
print(duplicate_count("Advertisement"), 3)
print(duplicate_count("problems solving"), 3)