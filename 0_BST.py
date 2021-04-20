# tree node definition
class Node(object):
    def __init__(self, value, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild

# tree definition
class Tree(object):
    def __init__(self, root=None):
        self.root = root

    # node in-order traversal(LDR)
    def traversal(self):
        traversal(self.root)

    # insert node
    def insert(self, value):
        self.root = insert(self.root, value)

    # delete node
    def delete(self, value):
        self.root = delete(self.root, value)

# node in-order traversal(LDR)
def traversal(node):
    if not node:
        return
    traversal(node.lchild)
    print(node.value,end=' ')
    traversal(node.rchild)

# insert node
def insert(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.lchild = insert(root.lchild, value)
    elif value > root.value:
        root.rchild = insert(root.rchild, value)
    return root

# delete node
def delete(root, value):
    if not root:
        return None
    if value < root.value:
        root.lchild = delete(root.lchild, value)
    elif value > root.value:
        root.rchild = delete(root.rchild, value)
    else:
        if root.lchild and root.rchild:  # degree of the node is 2
            target = root.lchild  # find the maximum node of the left subtree
            while target.rchild:
                target = target.rchild
            root = delete(root, target.value)
            root.value = target.value
        else:  # degree of the node is [0|1]
            root = root.lchild if root.lchild else root.rchild
    return root

if __name__ == '__main__':
    arr = [5, 3, 4, 0, 2, 1, 8, 6, 9, 7]
    T = Tree()
    for i in arr:
        T.insert(i)
    print('BST in-order traversal------------------')
    T.traversal()
    print('\ndelete test------------------')
    for i in arr[::-1]:
        print('after delete',i,end=',BST in-order is = ')
        T.delete(i)
        T.traversal()
        print()