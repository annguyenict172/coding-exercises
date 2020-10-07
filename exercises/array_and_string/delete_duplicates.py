"""
Delete duplicates from sorted array: EPI 5.5
"""


def delete_duplicates(A):
    write_idx = 1
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            A[write_idx] = A[i]
            write_idx += 1
    return write_idx


A = [1, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8]
delete_duplicates(A)
print(A)
