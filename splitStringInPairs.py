
def split_pairs(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result





print(split_pairs('abc'))
print(split_pairs('abcd'))
print(split_pairs('abcdef'))