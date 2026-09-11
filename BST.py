class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, value):
    new = Tree(value)
    if root is None:
        root = new
        return root
    current = root
    while True:    
        if value < current.data:
            if current.left is None:
                current.left = new
                break
            current = current.left
        else:
            if current.right is None:
                current.right = new
                break
            current = current.right
    return root

def display(root, space=0, level_space=5):

    if root is None:
        return

    # Print right subtree first
    display(root.right, space + level_space)

    # Print current node
    print()

    for i in range(space):
        print(" ", end="")

    print(root.data)

    # Print left subtree
    display(root.left, space + level_space)

root = None
values = [5,3,6,7,8,9]
for value in values:
    root = insert(root, value)
display(root)



