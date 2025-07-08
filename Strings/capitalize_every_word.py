def capitalize_text(string):
    list = string.split()
    new_list = [i.capitalize() for i in list]
    return ' '.join(new_list)

# Test cases
print(capitalize_text("hello world"))
print(capitalize_text("python programming is fun"))
print(capitalize_text("capitalize every word in this sentence"))