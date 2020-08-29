def n_queens(n):
    results = []

    for row in range(n):
        rows = [row]
        backtracking(1, n, rows, results)

    return results


def backtracking(col, n, rows, results):
    if col == n:
        results.append(rows[:])
        return

    for candidate in get_candidates(rows, col, n):
        rows.append(candidate)
        backtracking(col + 1, n, rows, results)
        rows.pop()


def get_candidates(rows, col, n):
    candidates = []
    for row in range(n):
        valid = True
        for other_col, other_row in enumerate(rows):
            if row == other_row \
                    or row + (col - other_col) == other_row\
                    or row - (col - other_col) == other_row:
                valid = False
                break
        if valid:
            candidates.append(row)
    return candidates


print(n_queens(4))
