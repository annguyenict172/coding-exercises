"""
Count the number of score combinations: EPI 16.1
"""


def number_of_score_combinations(total, individual_scores):
    num_combinations = [[1] + [0] * total for _ in individual_scores]

    for i in range(len(individual_scores)):
        for j in range(1, total+1):
            without_this_play = num_combinations[i - 1][j] if i > 0 else 0
            with_this_play = num_combinations[i][j - individual_scores[i]] if j - individual_scores[i] >= 0 else 0

            num_combinations[i][j] = without_this_play + with_this_play

    return num_combinations[-1][-1]


print(number_of_score_combinations(12, [2, 3, 7]))
