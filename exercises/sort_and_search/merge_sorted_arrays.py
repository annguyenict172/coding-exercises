"""
Merged sorted arrays in place: EPI 13.2
"""


def merge_sorted_arrays(A1, A2):
    # Push the first array forward
    first_empty_idx = A1.index(None)
    for i in range(0, first_empty_idx):
        A1[i], A1[i+first_empty_idx] = A1[i+first_empty_idx], A1[i]

    # Begin to sort the two arrays
    i, j, write_idx = first_empty_idx, 0, 0

    while i < len(A1) and A1[i] and j < len(A2):
        if A1[i] <= A2[j]:
            A1[write_idx] = A1[i]
            i += 1
        else:
            A1[write_idx] = A2[j]
            j += 1
        write_idx += 1

    # In case the second array is longer
    while j < len(A2):
        A1[write_idx] = A2[j]
        write_idx += 1
        j += 1


A1 = [3, 7, 11, 19, None, None, None, None, None]
A2 = [5, 10, 17]
merge_sorted_arrays(A1, A2)

print(A1)
