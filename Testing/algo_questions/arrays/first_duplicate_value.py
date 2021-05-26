def get_first_duplicate_value(array):
    if not array:
        return -1
    checked_values = {array[0]}

    for x in range(1, len(array)):
        if array[x] in checked_values:
            return array[x]
        checked_values.add(array[x])
    return -1


print(get_first_duplicate_value([2, 1, 5, 2, 3, 3, 4]))
