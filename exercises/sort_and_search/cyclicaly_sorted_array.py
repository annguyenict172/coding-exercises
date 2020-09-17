"""
Find the start index of a cyclicaly sorted array: EPI 11.3
"""


def find_start_idx(A):
    low, high = 1, len(A) - 1
    while low <= high:
        mid = (high + low) // 2
        if A[mid] < A[mid-1]:
            return mid
        
        if A[mid] > A[0]:
            low = mid + 1
        else:
            high = mid - 1
    return 0
