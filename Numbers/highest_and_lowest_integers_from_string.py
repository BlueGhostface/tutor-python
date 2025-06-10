def high_and_low(numbers):
    int_list = list(map(int, numbers.split()))
    highest = max(int_list)
    lowest = min(int_list)
    return f"{highest} {lowest}"




print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4") == "42 -9")
print(high_and_low("1 2 3" ) == "3 1")

