"""
Find intersection of two sorted arrays: EPI 13.1
"""


def intersection_of_sorted_arrays(l1, l2):
    intersection = []
    cur_i = -1

    cur_1, cur_2 = 0, 0
    while cur_1 < len(l1) and cur_2 < len(l2):
        if l1[cur_1] == l2[cur_2]:
            if cur_i < 0 or l1[cur_1] != intersection[cur_i]:
                intersection.append(l1[cur_1])
                cur_i += 1
            cur_1 += 1
            cur_2 += 1
        elif l1[cur_1] < l2[cur_2]:
            cur_1 += 1
        else:
            cur_2 += 1

    return intersection


print(intersection_of_sorted_arrays([2, 3, 3, 5, 5, 6, 7, 7, 8, 12], [5, 5, 6, 8, 8, 9, 10, 10]))
