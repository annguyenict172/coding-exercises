"""
Search a maze: EPI 18.1
"""


class SearchNode(object):
    def __init__(self, position, previous):
        self.position = position
        self.previous = previous


def search_maze(maze, start, end):
    visited = set()
    stack = [SearchNode(start, None)]
    has_path = False

    while len(stack):
        current = stack.pop()
        if current.position == end:
            has_path = True
            break
        visited.add(current.position)
        i, j = current.position

        if i > 0 and (i-1, j) not in visited and maze[i-1][j] == 0:
            stack.append(SearchNode((i-1, j), current))
        if i < len(maze)-1 and (i+1, j) not in visited and maze[i+1][j] == 0:
            stack.append(SearchNode((i+1, j), current))
        if j > 0 and (i, j-1) not in visited and maze[i][j-1] == 0:
            stack.append(SearchNode((i, j-1), current))
        if j < len(maze[0])-1 and (i, j+1) not in visited and maze[i][j+1] == 0:
            stack.append(SearchNode((i, j+1), current))

    if not has_path:
        return None

    path = []
    while current:
        path.append(current.position)
        current = current.previous
    path.reverse()

    return path


maze = [
    [1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0]
]

print(search_maze(maze, (5, 0), (0, 5)))
