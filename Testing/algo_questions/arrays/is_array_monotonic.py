array = [-1, -5, -10, -1100, -1101, -1102, -9000]


def is_monotonic(array):
    return (
            all(array[i] <= array[i + 1] for i in range(len(array) - 1)) or
            all(array[i] >= array[i + 1] for i in range(len(array) - 1))
    )

