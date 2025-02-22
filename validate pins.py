import re



def validate_pin(pin):
    return bool(re.fullmatch(r"\d{4}|\d{6}", pin))


print(validate_pin("1"))
print(validate_pin("12"))
print(validate_pin("1234"))

print(validate_pin("1234\n"))
print(validate_pin("123456\n"))

print(validate_pin("12345"))
print(validate_pin("123456"))
print(validate_pin("1234567"))