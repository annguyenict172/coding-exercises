"""
Sort an almost sorted array: EPI 10.3
"""
import heapq


def sort(A, k):
    min_heap = []
    heapq.heapify(min_heap)

    for item in A:
        if len(min_heap) >= k:
            print((heapq.heappop(min_heap)))
        heapq.heappush(min_heap, item)
    
    while len(min_heap):
        print((heapq.heappop(min_heap)))


sort([3, -1, 2, 6, 4, 5, 8], 2)
