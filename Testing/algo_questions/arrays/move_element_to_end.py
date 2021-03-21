array = [2, 1, 2, 2, 2, 3, 4, 2]
array_2 = [2, 2, 2, 2, 2]


def move_element_to_end(array, to_move):
    first_index_to_switch = None
    for index in range(len(array) - 1, -1, -1):
        current_element = array[index]
        if current_element == to_move:
            if index + 1 == len(array):
                continue
            if first_index_to_switch is None:
                continue
            element_from_first_available_index = array[first_index_to_switch]
            array[first_index_to_switch] = current_element
            array[index] = element_from_first_available_index
            first_index_to_switch -= 1
        else:
            if first_index_to_switch is None:
                first_index_to_switch = index
    return array


print(move_element_to_end(array_2, 2))
