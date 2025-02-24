def generate_hashtag(s):
    if len(s) <= 0:
        return False
    s = s.strip()
    s = "#" + s.title().replace(" ", "")

    if len(s) > 140:
        return False
    return s

print(generate_hashtag("Hello There")) # #HelloThere
print(generate_hashtag("            hello there        ")) # #HelloThere
print(generate_hashtag("hello thEre        ")) # #HelloThere
print(generate_hashtag("heLLo there")) # #HelloThere
