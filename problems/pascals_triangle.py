# give every row of Pascal's triangle as a list

# example
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1



def generate( numRows):
    pascal = []

    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        pascal.append(row)

    return pascal


print(generate(5))
print(generate(0))
print(generate(3))