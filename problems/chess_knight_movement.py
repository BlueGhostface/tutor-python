
from collections import deque

def knight(p1, p2):

    def to_coords(pos):
        col = ord(pos[0]) - ord('a')  # 'a' to 0, 'b' to 1, ...
        row = int(pos[1]) - 1         # '1' to 0, '2' to 1, ...
        return (row, col)

    def is_valid(x, y):
        return 0 <= x < 8 and 0 <= y < 8

    directions = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    start = to_coords(p1)
    end = to_coords(p2)

    if start == end:
        return 0

    visited = [[False for _ in range(8)] for _ in range(8)]
    queue = deque([(start[0], start[1], 0)])  # row, col, moves
    visited[start[0]][start[1]] = True

    while queue:
        x, y, moves = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (nx, ny) == end:
                return moves + 1

            if is_valid(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))

    return -1



moves = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))

def knight2(p1, p2):
    x, y = ord(p2[0])-97, int(p2[1])-1
    left, seen = deque([(ord(p1[0])-97, int(p1[1])-1, 0)]), set()
    while left:
        i, j, v = left.popleft()
        if i==x and j==y: return v
        if (i, j) in seen: continue
        seen.add((i, j))
        for a,b in moves:
            if 0 <= i+a < 8 and 0 <= j+b < 8:
                left.append((i+a, j+b, v+1))


def knight3(p1, p2):
    # start here!

    mask = [[0, 3, 2, 3, 2, 3, 4, 5, ],
            [3, 2, 1, 2, 3, 4, 3, 4, ],
            [2, 1, 4, 3, 2, 3, 4, 5, ],
            [3, 2, 3, 2, 3, 4, 3, 4, ],
            [2, 3, 2, 3, 4, 3, 4, 5, ],
            [3, 4, 3, 4, 3, 4, 5, 4, ],
            [4, 3, 4, 3, 4, 5, 4, 5, ],
            [5, 4, 5, 4, 5, 4, 5, 6, ]]

    corner = ['a1', 'a8', 'h1', 'h8']

    dx = abs(ord(p1[0]) - ord(p2[0]))
    dy = abs(ord(p1[1]) - ord(p2[1]))

    if dx == 1 and dy == 1 and ((p1 in corner) or (p2 in corner)):
        return 4
    else:
        return mask[dx][dy]



print(knight("a3", "b5"))  # Output: 1
print(knight("a1", "h8"))  # Output: 6
print(knight("e2", "e2"))  # Output: 0

print(knight2("a3", "b5"))  # Output: 1
print(knight2("a1", "h8"))  # Output: 6
print(knight2("e2", "e2"))  # Output: 0

print(knight3("a3", "b5"))  # Output: 1
print(knight3("a1", "h8"))  # Output: 6
print(knight3("e2", "e2"))  # Output: 0

