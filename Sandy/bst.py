class node:
    def __init__(self, key=None):
        self.parent = None
        self.key = key
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = node()

    def insert(self, key):
        if self.root.key is None:
            self.root.key = key
        else:
            item = node(key)
            x = self.root
            while x is not None:
                y = x
                if x.key > key:
                    x = x.left
                else:
                    x = x.right
            item.parent = y
            if y.key > key:
                y.left = item
            else:
                y.right = item

    def search(self, key):
        x = self.root
        while x is not None and x.key!=key:
            if x.key > key:
                x = x.left
            elif x.key < key:
                x = x.right
        return x

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print root.key,
            self.inorder(root.right)

    def min(self, root):
        while root.left is not None:
            root = root.left
        return root

    def max(self, root):
        while root.right is not None:
            root = root.right
        return root

    def delete(self, key):
        x = self.root
        while x is not None and x.key!=key:
            if x.key > key:
                x = x.left
            elif x.key < key:
                x = x.right
        if x is not None:
            y = x.parent
            if x.left is None and x.right is None:
                temp = None
            elif x.left is None:
                temp = x.right
                temp.parent = y
            elif x.right is None:
                temp = x.left
                temp.parent = y
            else:
                temp = self.min(x.right)
                if temp.parent.left == temp:
                    temp.parent.left = None
                else:
                    temp.parent.right = None
                temp.parent = y
            if y is not None:
                if y.left == x:
                    y.left = temp
                else:
                    y.right = temp
            else:
                if temp is not None:
                    self.root = temp
                else:
                    self.root = node()
        else:
            raise Exception('Node doesn\'t exist for key value %s' % key)
