def levenshtein_distance(s1, s2):
    table = [[0] * len(s1) for _ in range(len(s2))]

    # Initialize the top cell
    table[0][0] = 0 if s1[0] == s2[0] else 1

    # Initialize first cell of each row
    for i in range(1, len(s2)):
        table[i][0] = table[i-1][0] + 1

    # Initialize first cell of each column
    for j in range(1, len(s1)):
        table[0][j] = table[0][j-1] + 1

    for i in range(1, len(s2)):
        for j in range(1, len(s1)):
            min_dist = min(table[i-1][j-1], table[i-1][j], table[i][j-1])
            table[i][j] = min_dist if s2[i] == s1[j] else min_dist + 1

    return table[-1][-1]


print(levenshtein_distance('Sundays', 'Saturday'))
