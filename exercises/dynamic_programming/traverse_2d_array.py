"""
Find the number of ways to get from the top-left to bottom-right
of a 2D array. We can only go down and go right.
EPI 16.3
"""

def num_of_ways(n, m):
    def num_of_ways_to_pos(i, j, memos):
        if (i, j) in memos:
            return memos[(i, j)]
        if i == 0 and j == 0:
            return 1
        else:
            from_left = num_of_ways_to_pos(i, j-1, memos) if j > 0 else 0
            from_up = num_of_ways_to_pos(i-1, j, memos) if i > 0 else 0
            memos[(i, j)] = from_left + from_up
            return memos[(i, j)]
    
    return num_of_ways_to_pos(n-1, m-1, {})


print(num_of_ways(5, 5))
