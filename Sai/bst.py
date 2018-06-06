class Node:
    def __init__(self,key=None):
        self.left = None
        self.right = None
        self.value = key
        self.parent = None
#Binary search tree 
class BST:
    def __init__(self):
        self.root = Node()
    
    #Search Function for bst
    def search(self,key):
        val = self.root
        while val is not None and val.value != key:
            if val.value > key:
                val = val.left
            else:
                val = val.right
        return val
    def min(self,key):
        current = key
        while current.left is not None:
            current = current.left
        return current
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)
    #Insert function to add to the binary tree.
    def insert(self,key):
        if self.root.value is None:
            self.root.value = key
        else :
            item = Node(key)
            x = self.root
            while x is not None:
                y=x
                if x.value > key:
                    x = x.left
                else:
                    x = x.right
            item.parent = y
            if key < y.value:
                y.left = item
            else:
                y.right = item
    def deleteNode(self,root, key):
        # Base Case
        if root is None:
            return root 
    
        # If the key to be deleted is similiar than the root's
        # key then it lies in  left subtree
        if key < root.value:
            root.left = self.deleteNode(root.left, key)
    
        # If the kye to be delete is greater than the root's key
        # then it lies in right subtree
        elif(key > root.value):
            root.right = self.deleteNode(root.right, key)
    
        # If key is same as root's key, then this is the node
        # to be deleted
        else:
            
            # Node with only one child or no child
            if root.left is None :
                temp = root.right 
                root = None
                return temp 
                
            elif root.right is None :
                temp = root.left 
                root = None
                return temp
    
            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = min(root.right)
    
            # Copy the inorder successor's content to this node
            root.key = temp.key
    
            # Delete the inorder successor
            root.right = self.deleteNode(root.right , temp.key)
        return root 
    def delete(self,key):
        x = self.root
        #search the node to be deleted and assign it to x.
        x = self.search(key)
        #storing the parent of the node to deleted.
        y = x.parent
        if x is not None:
            #If node to be deleted is leaf node.
            if x.left is None and x.right is None:
                temp = None
            #if there is one child
            elif x.left is None:
                temp = x.right
                temp.parent = y
            elif x.right is None:
                temp = x.left
                temp.parent = y
            #if node has children on both sides
            else:
                temp = self.min(x.right)
                #delete the right minumum inorder successor
                if temp.parent.left == temp:
                    temp.parent.left = None
                else :
                    temp.parent.right = None
                #changing parent
                temp.parent = y
            if y is not None:
                if temp is None:
                    if y.left == x:
                        y.left = None
                    else:
                        y.right = None
                elif y.left == x:
                    y.left.value = temp.value
                else:
                    y.right.value = temp.value
            else:
                if temp is not None:
                    self.root.value = temp.value
                else:
                    self.root = Node()
        else:
            raise Exception('Node doesn\'t exist for key value %s' % key)

b = BST()
b.insert(50)
b.insert(30)
b.insert(20)
b.insert(40)
b.insert(70)
b.insert(60)
b.insert(80)
b.inorder(b.search(50))
b.delete(50)
print("afterdelete")
# x = b.search(50)
# print(x.value)
b.inorder(b.search(60))