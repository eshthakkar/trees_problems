# Helper classes and functions

class Node(object):
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None


def level_order_traversal(root):
    """Problem: Iterative implementation of level order traversal of a binary tree
        Time complexity: Using a queue, O(n)
        Space complexity: O(n) for the queue
    """

    q = [root]
    result = []

    while q:
        node = q.pop(0)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        result.append(node.val)

    return result    


def level_order_recursive(root):
    """ Problem: Recursive level order traversal of a tree using the call stack
        Time complexity : O(n^2) in worst case
    """

    result = []

    def print_given_level(root, level):
        if root is None:
            return

        if level == 1:
            result.append(root.val)
        elif level > 1:
            print_given_level(root.left, level - 1)
            print_given_level(root.right, level - 1)


    def heights(root):
        if root is None:
            return 0

        return 1 + max(heights(root.left), heights(root.right))

    h = heights(root)
    
    for i in xrange(1, h+1):
        print_given_level(root, i)

    return result    




# Tests
root = Node(1)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(4) 
root.right.right = Node(6)
out1 = level_order_traversal(root)
out2 = level_order_recursive(root)
assert out1 == out2, "Failed_outputs: out1: %s, out2: %s" %(out1, out2)


                
