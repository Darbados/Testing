"""
Here is the class which will represent the card itself.
"""


class Card(object):
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return "{0}{1}".format(self.name, self.color)