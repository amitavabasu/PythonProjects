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



"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def delete_from_bst(root, values_to_be_deleted):
    """
    Args:
     root(BinaryTreeNode_int32)
     values_to_be_deleted(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    if root == None: return root
    for val in values_to_be_deleted:
        curr = root
        prev = None
        while curr is not None:
            if val == curr.value:
                break
            elif val < curr.value:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right
        #Case-0-A value not found, nothing to delete
        if curr is None: return root
        #Case-0-B root is the value, delete root and return None
        if curr.left is None and curr.right is None:
            if prev is None:
                root = None
            else:
                if prev.left == curr:
                    prev.left = None
                else:
                    prev.right = None
        #Case-2 value node has only one child
        elif curr.left is None and curr.right is not None:
            if prev is None:
                root = curr.right
            else:
                if prev.left == curr:
                    prev.left = curr.right
                else:
                    prev.right = curr.right
        elif curr.right is None and curr.left is not None:
            if prev is None:
                root = curr.left
            else:
                if prev.left == curr:
                    prev.left = curr.left
                else:
                    prev.right = curr.left
        #Case-3 value node has both child, swap with predessor and remove predessor
        else:
            parent_pred = curr
            pred = curr.right
            while pred.left is not None:
                parent_pred = pred
                pred = pred.left
            curr.value = pred.value
            if parent_pred.left == pred:
                parent_pred.left = pred.right
            else:
                parent_pred.right = pred.right
    return root


def delete_from_bst_helper(root, key):
    if root is None:
        return root

    # Searching for a node with the given value.
    if key < root.value:
        root.left = delete_from_bst_helper(root.left, key)
    elif key > root.value:
        root.right = delete_from_bst_helper(root.right, key)
    else:
        # If the node to be deleted is a leaf node, then we will be replacing it with a NULL node.
        if root.left is None and root.right is None:
            del root
            return None

        # If the node to be deleted has only one child, then we will be replacing it with its non-NULL child.
        if root.left is None:
            temp = root.right
            del root
            return temp
        if root.right is None:
            temp = root.left
            del root
            return temp

        # If the node to be deleted has two child nodes, then we will be replacing its value with that of its
        # inorder successor and recursively delete the inorder successor.
        temp = root.right
        while temp.left is not None:
            temp = temp.left
        root.value = temp.value
        root.right = delete_from_bst_helper(root.right, temp.value)

    return root

def delete_from_bst2(root, values_to_be_deleted):
    if root is None or len(values_to_be_deleted) == 0:
        return root

    for value in values_to_be_deleted:
        root = delete_from_bst_helper(root, value)

    return root


if __name__ == "__main__":
    print(build_a_bst([1, 2, 3, 4, 5]))