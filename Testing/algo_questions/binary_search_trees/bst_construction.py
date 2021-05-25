class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'BST node with value {self.value}'

    def get_min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def remove(self, value, parent=None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.get_min_value()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.rigt
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    # Single node, do not do anything
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.right if self.right is not None else self.left
        return self

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = self.build(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = self.build(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        if self.value == value:
            return True
        if self.value < value:
            if self.right:
                return self.right.contains(value)
            return False
        else:
            if self.left:
                return self.left.contains(value)
            return False

    def traverse_in_order_ascending(self):
        if self.value:
            if self.left:
                self.left.traverse_in_order_ascending()
            print(self)
            if self.right:
                self.right.traverse_in_order_ascending()

    @classmethod
    def build(cls, value):
        return cls(value)


bst_tree = BST(8)
bst_tree.insert(10)
bst_tree.insert(14)
bst_tree.insert(13)
bst_tree.insert(3)
bst_tree.insert(2)
bst_tree.insert(1)
bst_tree.insert(4)
bst_tree.insert(7)
print(bst_tree.contains(7))
print(bst_tree.contains(25))
bst_tree.traverse_in_order_ascending()
