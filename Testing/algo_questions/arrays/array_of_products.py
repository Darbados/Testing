import math


def get_array_of_products(array):
    result_array = []

    for idx, x in enumerate(array):
        result_array.append(math.prod(e for ii, e in enumerate(array) if idx != ii))
    return result_array


print(get_array_of_products([5, 1, 4, 2]))
