import heapq


def merge_sorted_arrays(arrays):
    final_list = []

    # This is to keep track of where we at in each array_and_string
    last_index = [0] * len(arrays)

    # Initialize the min heap with the first element from each array_and_string
    min_heap = [(a[0], array_index) for array_index, a in enumerate(arrays) if len(a)]
    heapq.heapify(min_heap)

    while len(min_heap):
        # Get the minimum number along with the array_and_string where it comes from
        num, array_index = heapq.heappop(min_heap)

        final_list.append(num)

        # Increment the write index for this array_and_string
        last_index[array_index] += 1

        # Check if there is any other number in this array_and_string
        if last_index[array_index] == len(arrays[array_index]):
            continue
        else:
            # If not, we will push the next number in this array_and_string into the min heap
            next_number = arrays[array_index][last_index[array_index]]
            heapq.heappush(min_heap, (next_number, array_index))
    return final_list


def get_increasing_sub_arrays(array):
    sub_arrays = []
    current = []

    for i in range(0, len(array)-2):
        if array[i] <= array[i+1]:
            current.append(array[i])
        else:
            if len(current):
                sub_arrays.append(current[:])
                current = []
            else:
                continue

    # Check the last element
    if array[-1] and len(current):
        current.append(array[-1])
        sub_arrays.append(current[:])

    return sub_arrays


def sort_increasing_decreasing_array(array):
    increasing_sub_arrays = get_increasing_sub_arrays(array)
    array.reverse()
    increasing_sub_arrays += get_increasing_sub_arrays(array)

    sorted_array = merge_sorted_arrays(increasing_sub_arrays)
    return sorted_array


print(sort_increasing_decreasing_array([1, 4, 7, 12, 11, 10, 9, 15, 18, 30, 29, 28, 27]))
