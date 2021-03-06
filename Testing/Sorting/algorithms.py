"""
Module containing sorting algorithms
"""


def bubble_sort(array):
    for x in range(len(array)-1, 0, -1):
        for y in range(x):
            if array[y] > array[y+1]:
                temp = array[y]
                array[y] = array[y+1]
                array[y+1] = temp


def selection_sort(array):
    for x in range(len(array)):
        for y in range(x + 1, len(array)):
            if array[y] < array[x]:
                temp = array[x]
                array[x] = array[y]
                array[y] = temp


def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left_half = array[:middle]
    right_half = array[middle:]

    merge_sort(left_half)
    merge_sort(right_half)

    x = 0
    y = 0
    z = 0

    while x < len(left_half) and y < len(right_half):
        if left_half[x] < right_half[y]:
            array[z] = left_half[x]
            x = x + 1
        else:
            array[z] = right_half[y]
            y = y + 1
        z = z + 1

    while x < len(left_half):
        array[z] = left_half[x]
        x = x + 1
        z = z + 1

    while y < len(right_half):
        array[z] = right_half[y]
        y = y + 1
        z = z + 1
