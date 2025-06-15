def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)


print(solution('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']), 'apples, pears\ngrapes\nbananas')
print(solution('apples pears bananas // otherfruit', ['/']), 'apples pears bananas')
print(solution('pineapple $ apple ', ['$']), ' pineapple')