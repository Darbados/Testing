array = [-1, -5, -10, -1100, -1101, -1102, -9000]


def is_monotonic(array):
    if not array:
        return True
    if len(array) == 1:
        return True

    increasing, decreasing = array[0] < array[1], not array[0] < array[1]
    for el in array[1:]:
        if increasing and el < array[0]:
            return False
        if decreasing and el > array[0]:
            return False
    return True


print(is_monotonic([1, 2, 3, 4, -1]))
