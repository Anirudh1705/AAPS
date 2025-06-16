from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class LevelOrderTree:
    def __init__(self):
        self.root = None

    def print_level_order(self):
        if not self.root:
            return
        queue = deque()
        queue.append(self.root)
        while queue:
            temp_node = queue.popleft()
            print(temp_node.data, end=' ')
            if temp_node.left:
                queue.append(temp_node.left)
            if temp_node.right:
                queue.append(temp_node.right)

if __name__ == "__main__":
    tree = LevelOrderTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print("Level order traversal of binary tree is:")
    tree.print_level_order()
