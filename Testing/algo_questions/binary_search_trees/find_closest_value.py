"""
We have a BST, and target value. We need to find the closest value to target value from the BST.
BST is such Binary Tree, where all nodes in left has values less than the root, and all the values
in right has greater values than root. Nodes must be distinct. Nodes should also form valid
BST subtrees.
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'Value: {self.value}, Left node: {self.left}, Right node: {self.right}'


bst = BST(10)
bst.right = BST(15)
bst.right.left = BST(12)
bst.left = BST(8)
bst.left.left = BST(6)


def find_value_recursion(bst, value):
    if bst is None or bst.value == value:
        return bst

    if bst.root > value:
        return find_value_recursion(bst.left, value)
    elif bst.root < value:
        return find_value_recursion(bst.right, value)


def find_closest_value(bst, target_value):
    current_node = bst
    closest = current_node.value
    while current_node is not None:
        if abs(target_value - closest) > abs(target_value - current_node.value):
            closest = current_node.value
        if current_node.value > target_value:
            current_node = current_node.left
        elif current_node.value < target_value:
            current_node = current_node.right
        else:
            break
    return closest


def find_value_looping(bst, value):
    current_node = bst
    while current_node is not None:
        if current_node.value == value:
            return current_node
        if current_node.value > value:
            current_node = current_node.left
        else:
            current_node = current_node.right


# print(find_value_recursion(bst, 8))
# print(find_value_looping(bst, 8))
print(find_closest_value(bst, 13))
