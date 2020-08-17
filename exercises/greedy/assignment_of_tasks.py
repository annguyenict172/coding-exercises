"""
Compute an optimum assignment of tasks: EPI 17.1
"""


def assign_tasks(tasks):
    tasks.sort()
    scheduled_tasks = []
    low, high = 0, len(tasks) - 1
    while low < high:
        scheduled_tasks.append((tasks[low], tasks[high]))
        low += 1
        high -= 1

    return scheduled_tasks


print(assign_tasks([5, 2, 1, 6, 4, 4]))
