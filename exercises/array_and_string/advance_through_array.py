"""
Advancing through an array: EPI 5.4
"""


def can_advance_through_array(A):
    furthest_idx = 0
    for i in range(len(A)):
        if A[i] == 0 and furthest_idx <= i:
            return False
        else:
            furthest_idx = max(furthest_idx, A[i] + i)

    return True


print(can_advance_through_array([1, 1, 1, 0, 2, 0, 1]))
