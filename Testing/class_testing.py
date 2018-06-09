"""
Some class internal stuff testing
"""

class Name(object):
    def __init__(self, name):
        self.name = name
        self.name_length = len(self.name)

    @property
    def length(self):
        return self.name_length