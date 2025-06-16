class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Inorder Traversal (Left, Root, Right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

# Preorder Traversal (Root, Left, Right)
def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

# Postorder Traversal (Left, Right, Root)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')

# Example usage
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal:", end=' ')
    inorder(root)
    print("\nPreorder traversal:", end=' ')
    preorder(root)
    print("\nPostorder traversal:", end=' ')
    postorder(root)
    print()
