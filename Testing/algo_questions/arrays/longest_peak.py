test_array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]


def get_longest_peak(array):
    longest_peak = 0
    current_idx = 0

    while current_idx < len(array) - 1:
        if array[current_idx - 1] < array[current_idx] > array[current_idx + 1]:
            current_peak = 3
            left_peak_side = current_idx - 2
            right_peak_side = current_idx + 2
            while left_peak_side >= 0:
                if array[left_peak_side] < array[left_peak_side + 1]:
                    current_peak += 1
                    left_peak_side -= 1
                else:
                    break
            while right_peak_side <= len(array) - 1:
                if array[right_peak_side] < array[right_peak_side - 1]:
                    current_peak += 1
                    right_peak_side += 1
                else:
                    break
            longest_peak = current_peak
        current_idx += 1

    return longest_peak


print(get_longest_peak(test_array))
