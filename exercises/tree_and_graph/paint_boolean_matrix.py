"""
Paint a boolean matrix: EPI 18.2
"""


def paint_matrix(M, entry):
    visited = set()
    stack = [entry]

    entry_color = M[entry[0]][entry[1]]

    while len(stack):
        i, j = stack.pop()

        # Flip the color
        M[i][j] = not entry_color

        # Add to visited set
        visited.add((i, j))

        if i > 0 and (i-1, j) not in visited and M[i-1][j] == entry_color:
            stack.append((i-1, j))
        if i < len(M)-1 and (i+1, j) not in visited and M[i+1][j] == entry_color:
            stack.append((i+1, j))
        if j > 0 and (i, j-1) not in visited and M[i][j-1] == entry_color:
            stack.append((i, j-1))
        if j < len(M[0])-1 and (i, j+1) not in visited and M[i][j+1] == entry_color:
            stack.append((i, j+1))


matrix = [
    [True, True, True, True, True],
    [True, True, True, True, True],
    [True, True, True, True, True],
    [True, True, True, True, True],
    [False, False, False, False, False],
    [False, True, True, True, False],
    [False, True, True, True, False],
    [False, True, True, True, False],
    [False, True, True, True, False],
]

paint_matrix(matrix, (6, 2))

print(matrix)
