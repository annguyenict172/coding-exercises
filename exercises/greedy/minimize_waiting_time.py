"""
Execute task in an order such that the waiting time is minimized: EPI 17.2
"""


def minimize_waiting_time(service_times):
    service_times.sort()
    total_waiting_time = 0
    running_sum = 0

    for i in range(1, len(service_times)):
        running_sum += service_times[i-1]
        total_waiting_time += running_sum

    return total_waiting_time


print(minimize_waiting_time([2, 5, 3, 1]))
