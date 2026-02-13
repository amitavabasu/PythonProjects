class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_a_bst(values):
    """
    Args:
     values(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    root = None
    for val in values:
        root = insert_in_bst(root, val)
    return root


def insert_in_bst(root, val):
    if root is None:
        root = BinaryTreeNode(val)
        return root
    curr = root
    parent = None
    while curr is not None:
        parent = curr
        if val <= curr.value:
            curr = curr.left
        else:
            curr = curr.right
    if val <= parent.value:
        parent.left = BinaryTreeNode(val)
    else:
        parent.right = BinaryTreeNode(val)
    return root

if __name__ == "__main__":
    print(build_a_bst([1, 2, 3, 4, 5]))