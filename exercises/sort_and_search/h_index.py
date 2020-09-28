"""
Compute the h-index: EPI 13.3
"""

def compute_h_index(citations):
    citations.sort()
    n = len(citations)
    
    for i, c in enumerate(citations):
        if c >= n - i:
            return n - i
    
    return 0



print(compute_h_index([12, 9, 11, 17, 4, 14, 10, 13, 16]))