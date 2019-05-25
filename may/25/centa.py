# Implicit graph problem
# This is a BFS
from collections import deque


DIRECTIONS = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]


def is_path(x, y, board):
    M, N = len(board), len(board[0])

    return (x >= 0 and x < N and
            y >= 0 and y < M and
            not board[x][y])


def min_number_of_steps(start, end, board):
    parent = {}
    visited = set()
    queue = deque()

    parent[start] = start
    queue.append(start)

    # find best path with BFS
    while queue:
        curr = queue.popleft()
        visited.add(curr)
        x, y = curr

        for dx, dy in DIRECTIONS:
            if (is_path(x + dx, y + dy, board) and
                (x + dx, y + dy) not in visited):
                
                parent[(x + dx, y + dy)] = curr
                queue.append((x + dx, y + dy))

    if end not in visited:
        return -1

    # Count the number of steps on the path found
    steps = 0
    curr = end
    while parent[curr] != curr:
        curr = parent[curr]
        steps += 1

    return steps


if __name__ == "__main__":
    board = [[ False, False, False, False],
             [  True,  True, False,  True],
             [ False, False, False, False],
             [ False, False, False, False]]
            
    start = ( 3, 0)
    end = ( 0, 0)

    print(min_number_of_steps(start, end, board))