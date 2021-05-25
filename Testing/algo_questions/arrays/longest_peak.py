test_array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]


def get_longest_peak(array):
    current_peak = array[0]
    peaks = {}

    for x in range(1, len(array) - 1):
        if current_peak <= array[x]:
            continue
        current_peak = array[x]
