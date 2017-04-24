def find_min_bst(root):

    if not root:
        return root

    if not root.left:
        return root.value
    
    return find_min_bst(root.left)
    
    
class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None 


def add_node_bst(root,key):
    """Add a node to a BST"""

    if root is None:
        return Node(key)

    if key < root.value:
        root.left = add_node_bst(root.left,key)
    elif key > root.value:
        root.right = add_node_bst(root.right,key)

    return root


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


# Driver program

# Test 1
eleven = Node(11)
root = eleven
add_node_bst(root, 4)
add_node_bst(root, 6)
add_node_bst(root, 15)
add_node_bst(root, 8)
add_node_bst(root, 14)
add_node_bst(root, 1)
print inorder(root)
print find_min_bst(root)

# Test 2
root = Node(6)
print find_min_bst(root)

# Test 3
print find_min_bst(None)

# Test 4
root = Node(3)
add_node_bst(root, 5)
add_node_bst(root, 6)
add_node_bst(root, 4)
print find_min_bst(root)
