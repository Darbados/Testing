test_array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]


def get_longest_peak(array):
    peaks = {}
    max_peak_number = None
    current_peak_key = None
    current_idx = 0

    # Need refactor for current_peak_key reset.
    # Should remove peaks that are not actual peaks.

    while current_idx < len(array) - 1:
        if current_idx == 0:
            if array[current_idx + 1] <= array[current_idx]:
                current_idx += 1
            else:
                max_peak_number = array[current_idx]
                current_peak_key = array[current_idx]
                peaks[current_peak_key] = 1
                current_idx += 1
        else:
            if max_peak_number < array[current_idx]:
                max_peak_number = array[current_idx]
                peaks[current_peak_key] += 1
                current_idx += 1
            elif max_peak_number == array[current_idx]:
                current_idx += 1
                current_peak_key = None
            else:
                peaks[current_peak_key] += 1
                current_idx += 1


get_longest_peak(test_array)
