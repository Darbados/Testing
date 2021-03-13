"""
Three numbers sum problem.

We have an array of distinct integers, and integer representing the target_sum.
We need to find each unique combination of 3 integers that sum up to the target sum.
Those should be returned as an array for each combo, gathered in a parent array. So
the output should be two dimensional arrays with the combinations. Triplets should be
ordered ascending.
If no triplets are available, [] should be returned.

Approach 1, Brute force:
Use 3 nested loops to iterate over the array to find if 3 numbers sum up to target_sum.
Time complexity O(N^3) - cubic.

Approach 2:
Use a dict, to store each combo of 2 distinct ints as a key, where the value is always the
target_sum.

After dict is filled, we iterate over the array, trying to find is z = target_sum - (x + y) is
within the numbers
"""

numbers = [12, 3, 1, 2, -6, 5, -8, 6]


def three_numbers_sum(array, target_sum):
    x_y_sum_dict = {}
    x_y_z_sum_dict = {}
    tracked_idx = 0

    while tracked_idx < len(array):
        processed_number = numbers[tracked_idx]

        for idx, n in enumerate(array):
            if idx <= tracked_idx:
                continue
            x_y_sum_dict[processed_number, n] = target_sum
        tracked_idx += 1

    for x_y, target_sum in x_y_sum_dict.items():
        z = target_sum - sum(x_y)
        if z in numbers and z not in x_y:
            x_y_z_key = list(x_y + (z,))
            x_y_z_key.sort()
            x_y_z_sum_dict[tuple(x_y_z_key)] = target_sum

    return sorted([list(x_y_z) for x_y_z in x_y_z_sum_dict.keys()])


print(three_numbers_sum(numbers, 0))


# Algo expert solution:
# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
        return triplets
