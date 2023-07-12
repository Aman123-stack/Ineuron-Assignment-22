q1> class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def binary_tree_to_dll(root):
    if root is None:
        return None

    # Convert the left subtree to DLL
    left_head = binary_tree_to_dll(root.left)

    # Find the inorder predecessor (rightmost node) in the left subtree
    prev = None
    current = left_head
    if current:
        while current.right:
            current = current.right
        prev = current

    # Convert the root to a DLL node and link it with the predecessor
    root.left = prev
    if prev:
        prev.right = root

    # Convert the right subtree to DLL and get its head
    right_head = binary_tree_to_dll(root.right)

    # Link the root with the head of the right subtree
    root.right = right_head
    if right_head:
        right_head.left = root

    # Return the head of the resulting DLL
    if left_head:
        return left_head
    else:
        return root




q2># Create a binary tree
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

# Convert the binary tree to DLL
head = binary_tree_to_dll(root)

# Print the doubly linked list
current = head
while current:
    print(current.data, end=" ")
    current = current.right





q3>class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def flip_binary_tree(root):
    # Base case: if the root is None or a leaf node
    if root is None or (root.left is None and root.right is None):
        return root

    # Recursively flip the left and right subtrees
    flipped_left = flip_binary_tree(root.left)
    flipped_right = flip_binary_tree(root.right)

    # Swap the left and right children of the root
    root.left = flipped_right
    root.right = flipped_left

    return root






q4>class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_root_to_leaf_paths(root):
    if root is None:
        return

    stack = [(root, str(root.data))]  # Initialize stack with root and its path
    while stack:
        node, path = stack.pop()

        # If the node is a leaf, print the path
        if node.left is None and node.right is None:
            print(path)

        # Push the right child to the stack if it exists
        if node.right:
            stack.append((node.right, path + '->' + str(node.right.data)))

        # Push the left child to the stack if it exists
        if node.left:
            stack.append((node.left, path + '->' + str(node.left.data)))


# Create a binary tree
root = Node(6)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(4)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

# Print all root-to-leaf paths
print_root_to_leaf_paths(root)
