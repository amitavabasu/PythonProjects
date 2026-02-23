

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    result = []
    if root is None: return result
    queue = [root]
    while queue:
        element = queue.pop(0)
        result.append(element.value)
        if element.left is not None:
            queue.append(element.left)
        if element.right is not None:
            queue.append(element.right)
    return result

if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    # root.right = BinaryTreeNode(3)
    # root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    # root.right.left = BinaryTreeNode(6)
    root.left.right.left = BinaryTreeNode(7)
    print(level_order_traversal(root))