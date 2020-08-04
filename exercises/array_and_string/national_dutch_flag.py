"""
National Dutch Flag partition: EPI 5.1
"""


def dutch_flag_partition(A, pivot_index):
    pivot = A[pivot_index]

    # Maintain three sub arrays: smaller, equal and larger
    # smaller is the largest index of the smaller subarray
    # larger is the smallest index of the larger subarray
    smaller, equal, larger = 0, 0, len(A) - 1
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
        elif A[equal] > pivot:
            A[larger], A[equal] = A[equal], A[larger]
            larger -= 1
        equal += 1
