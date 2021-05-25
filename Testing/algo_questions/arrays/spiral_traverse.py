test_array = [
    [2, 3, 4, 8],
    [4, 5, 6, 7],
    [10, 11, 9, 3],
    # [15, 20, 0, -9],
]


def spiral_traverse(array):
    assert len(array)

    start_row, end_row = 0, len(array) - 1
    start_col, end_col = 0, len(array[0]) - 1
    result = []

    while start_row <= end_row and start_col <= end_col:
        for col in range(start_col, end_col + 1):
            # Traverse top border
            result.append(array[start_row][col])

        for row in range(start_row + 1, end_row + 1):
            # Traverse right border
            result.append(array[row][end_col])

        for col in reversed(range(start_col, end_col)):
            # Traverse bottom border
            if start_row == end_row:
                # Handle edge case with a single row in the middle of the matrix.
                # We don't want to count it twice, as we've already checked it in the previous
                # loop.
                break
            result.append(array[end_row][col])

        for row in reversed(range(start_row + 1, end_row)):
            # Traverse left border

            if start_col == end_col:
                # Handle edge case with a single column in the middle of the matrix.
                # We don't want to count it twice, as we've already checked it in the first
                # loop.
                break
            result.append(array[row][start_col])

        # Prepare for inner parameter traverse
        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1
    return result
