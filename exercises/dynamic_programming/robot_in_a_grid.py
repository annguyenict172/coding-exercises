"""
Robot In a Grid

We have a grid (m x n) and a robot at (0,0)
The robot can only move right and down, and there are certain spots
that the robot cannot step on
Find a path for the robot to reach the bottom right corner

Sample Input:
5
5
1 1 1 1 1 1 1 1 1 1 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1

Sample Output:
(0,0), (1,0), (1,1), (1,2), (2,2), (3,2), (4,2), (4,3), (4,4)
"""

from io import StringIO
import unittest


def find_path_for_robot(stdin):
    # Parse the input to build a grid
    m = n = 0
    grid = []
    for line_no, line in enumerate(stdin):
        if line_no == 0:
            m = int(line)
        elif line_no == 1:
            n = int(line)
        else:
            line = list(reversed(line.split()))
            for row in range(m):
                current_row = []
                for col in range(n):
                    current_row.append(int(line.pop()))
                grid.append(current_row)

    paths = [[0 for _ in range(n)] for _ in range(m)]
    paths[0][0] = 1

    # Mark the points that we can reach
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 0 or paths[row][col] == 0:
                continue
            if row+1 <= m-1 and grid[row+1][col] == 1:
                paths[row+1][col] = 1
            if col+1 <= n-1 and grid[row][col+1] == 1:
                paths[row][col+1] = 1

    # If we cannot reach the destination, no path is found
    if paths[m-1][n-1] == 0:
        return None, grid

    # Traceback to get the path
    next_point = (m-1, n-1)
    path = [next_point]
    while next_point != (0, 0):
        row, col = next_point
        if row-1 >= 0 and paths[row-1][col]:
            next_point = (row-1, col)
        else:
            next_point = (row, col-1)
        path.append(next_point)

    return list(reversed(path)), grid


def verify_path(path, grid):
    height = len(grid)
    width = len(grid[0])

    if path[0] != (0,0):
        return False
    if path[-1] != (height-1, width-1):
        return False
    for i in range(0, len(path)-1):
        point = path[i]
        next_point = path[i+1]

        is_on_the_right = point[0] == next_point[0] and point[1]+1 == next_point[1]
        is_below = point[0]+1 == next_point[0] and point[1] == next_point[1]

        if is_on_the_right or is_below:
            continue
        else:
            return False
    return True


class TestResult(unittest.TestCase):

    def test_5x5_grid(self):
        stdin = StringIO('5\n5\n1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n')
        path, grid = find_path_for_robot(stdin)
        self.assertTrue(verify_path(path, grid))

    def test_5x5_grid_with_unreachable_cells(self):
        stdin = StringIO('5\n5\n1 1 1 1 1 0 0 1 1 1 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1\n')
        path, grid = find_path_for_robot(stdin)
        self.assertTrue(verify_path(path, grid))

    def test_no_solution(self):
        stdin = StringIO('5\n5\n1 1 1 1 1 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1\n')
        path, grid = find_path_for_robot(stdin)
        self.assertIsNone(path)
