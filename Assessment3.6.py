class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(letters):
    nodes = [Node(ch) for ch in letters]
    for i, node in enumerate(nodes):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0]

def preorder(node, result):
    if node:
        result.append(node.data)
        preorder(node.left, result)
        preorder(node.right, result)

def inorder(node, result):
    if node:
        inorder(node.left, result)
        result.append(node.data)
        inorder(node.right, result)

def postorder(node, result):
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.data)

root = build_tree("MARKJUSTINNAVAJA")

for name, func in [("PreOrder", preorder), ("InOrder", inorder), ("PostOrder", postorder)]:
    result = []
    func(root, result)
    print(f"{name}: {' '.join(result)}")