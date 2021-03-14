

array_one = [-1, 5, 10, 20, 28, 3]
array_two = [26, 134, 135, 15, 17]


# All test cases in Algo Experts are passed
def get_smallest_difference(array_one, array_two):
    smallest_diff = None
    tracked_idx = 0
    smallest_diff_el_one, smallest_diff_el_two = None, None

    while tracked_idx < len(array_one):
        x = array_one[tracked_idx]
        for idx, y in enumerate(array_two):
            if smallest_diff is None or abs(x - y) < smallest_diff:
                smallest_diff = abs(x - y)
                smallest_diff_el_one, smallest_diff_el_two = tracked_idx, idx
        tracked_idx += 1

    return [array_one[smallest_diff_el_one], array_two[smallest_diff_el_two]]


print(get_smallest_difference(array_one, array_two))


# Algo expert solution -- Uhh, seems it don't work
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float('inf')
    current = float('inf')
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = firstNum, secondNum
        return smallestPair
