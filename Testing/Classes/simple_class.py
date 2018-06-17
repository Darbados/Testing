"""
Simple class that will have method which will accept input and set its value in the class and printing uppercase method
"""


class SimpleClass:
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input("Write anything here: ")

    def print_upper(self):
        print(self.s.upper())