class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.value = key

class binary_search_tree:
    def __init__(self):
        self.root = node()

    def insert(self, input_value):
        if self.root.key is None:
            self.root.key = key
        else:
            item = node(input_value)
            x = self.root
            while x is not None:
                y = x
                if x.key < input_value:
                    x = x.right
                else:
                    x = x.left
            item.parent = y
            if y.value < input_value:
                y.left = item
            else:
                y.right = item

    def find_minimum(self, item):
        while item.left is not None:
            item = item.left
        return item

    def transplant(self, node1, node2):
        if node1 is None:
            self.root = node2
        elif node1.value == node1.parent.left.value:
            node1.parent.left = node2
        else:
            node1.parent.right = node2
        if node2 is not None:
            node2.parent = node1.parent

    def delete(self, deleting_node):
        if deleting_node.left is None:
            self.transplant(deleting_node, deleting_node.right)
        elif deleting_node.right is None:
            self.transplant(deleting_node, deleting_node.left)
        else:
            y = self.find_minimum(deleting_node.right)
            if y.parent != deleting_node:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(deleting_node, y)
            y.left = deleting_node.left
            y.left.parent = y

    def search(self, value):
        if self.value == value or (self.right == None and self.left == None):
            return self
        else:
            if value <  self.value :
                return search(self.left, value)
            else:
                return search(self.right, value)
