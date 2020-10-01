"""
Compute enclosed regions: EPI 18.3
"""
import collections

def compute_enclosed_regions(A):
    seen = set()
    queue = collections.deque()
    m, n = len(A), len(A[0])

    # Find the W on the first row and the last row
    for j in range(0, n):
        if A[0][j] == 'W':
            queue.append((0, j))
        if A[m-1][j] == 'W':
            queue.append((m-1, j))
    
    # Find the W on the first column and the last column
    for i in range(1, m-1):
        if A[i][0] == 'W':
            queue.append((i, 0))
        if A[i][n-1] == 'W':
            queue.append((i, n-1))
    
    # Start with the Ws which are on the boundary to see which other Ws we can reach to
    while len(queue):
        i, j = queue.popleft()
        seen.add((i, j))
        # Temporarily paint it with Y
        A[i][j] = 'Y'
        
        if i > 0 and (i-1, j) not in seen and A[i-1][j] == 'W':
            queue.append((i-1, j))
        if i < m-1 and (i+1, j) not in seen and A[i+1][j] == 'W':
            queue.append((i+1, j))
        if j > 0 and (i, j-1) not in seen and A[i][j-1] == 'W':
            queue.append((i, j-1))
        if j < n-1 and (i, j+1) not in seen and A[i][j+1] == 'W':
            queue.append((i, j+1))
    
    # Repaint Y with W (since we can reach them from the boundary), and W with B
    for i in range(m):
        for j in range(n):
            if A[i][j] == 'Y':
                A[i][j] = 'W'
            elif A[i][j] == 'W':
                A[i][j] = 'B'
    return A

A = [
    ['B', 'B', 'B', 'B'],
    ['W', 'B', 'W', 'B'],
    ['B', 'W', 'W', 'B'],
    ['B', 'B', 'B', 'B']
]

print(compute_enclosed_regions(A))
