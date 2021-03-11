"""
Attempt for implementing Iterator with Python 36
"""


class Iterator:
    def __init__(self, array):
        assert type(array) == list

        self.array = array
        self.current = 0

    def current_element(self):
        return self.array[self.current]

    def next(self):
        self.current += 1
        return self.array[self.current]

    def prev(self):
        self.current -= 1
        return self.array[self.current]

    def is_done(self):
        return
