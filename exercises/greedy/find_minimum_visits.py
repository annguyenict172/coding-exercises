"""
The interval covering problem: EPI 17.3
"""

# This function assumes that interval 1 starts earlier than interval 2
def get_overlap(itv1, itv2):
    # Special case: There is no overlap
    if itv1[1] < itv2[0]:
        return None
    # Special case: Interval 1 wraps around Interval 2
    elif itv1[1] >= itv2[1]:
        return itv2
    else:
        return (itv2[0], itv1[1])


def find_minimum_visits(intervals):
    # Sort the intervals by starting time
    intervals.sort(key=lambda x: x[0])

    visit_interval = intervals[0]
    visit_time = 1
    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        overlap = get_overlap(visit_interval, current_interval)
        if not overlap:
            visit_interval = current_interval
            visit_time += 1
        else:
            visit_interval = overlap
    
    return visit_time


print(find_minimum_visits([(0, 3), (2, 6), (3, 4), (6, 9)]))
print(find_minimum_visits([(1, 2), (2, 3), (3, 4), (2, 3), (3, 4), (4, 5)]))