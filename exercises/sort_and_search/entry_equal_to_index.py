"""
Search for an entry which is equal to its index: EPI 11.2
"""


def find_entry_equal_to_index(A):
    low, high = 0, len(A)-1
    while low <= high:
        mid = (low + high) // 2
        if mid == A[mid]:
            return mid
        elif mid < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
