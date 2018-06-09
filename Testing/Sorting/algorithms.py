"""
File which will hold some sorting algorithms
"""


class SortAlgorithms:
    def __init__(self, to_sort):
        self.to_sort = to_sort

    def bubble_sort(self):
        for x in range(len(self.to_sort), 0, -1):
            for y in range(x):
                if self.to_sort[x] > self.to_sort[y]:
                    temp = self.to_sort[x]
                    self.to_sort[x] = self.to_sort[y]
                    self.to_sort[y] = temp

    def selection_sort(self):
        for x in range(len(self.to_sort)):
            for y in range(x + 1, len(self.to_sort)):
                if self.to_sort[y] < self.to_sort[x]:
                    temp = self.to_sort[x]
                    self.to_sort[x] = self.to_sort[y]
                    self.to_sort[y] = temp

    def merge_sort(self, array):
        if len(array) > 1:
            middle = len(array) // 2
            left_half = array[:middle]
            right_half = array[middle:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

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