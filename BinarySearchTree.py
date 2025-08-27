class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def inorder(self):
        self._inorder(self.root)
    
    def _inorder(self, root):
        if root is None:
            return
        self._inorder(root.left)
        print(root.value, end = " ")
        self._inorder(root.right)
        
    def insert(self, value):
        self.root = self._insert(value, self.root)
    
    def _insert(self, value, root):
        new_node = Node(value)
        if root is None:
            return new_node
        if value >= root.value:
            root.right = self._insert(value, root.right)
        else:
            root.left = self._insert(value, root.left)
        return root

    def search(self, key):
        return self._search(key, self.root)
    
    def _search(self, key, root):
        if root is None: # not found
            return False
        result = False
        if key < root.value:
            result = self._search(key, root.left)
        elif key > root.value:
            result = self._search(key, root.right)
        else: # key == value
            return True
        return result
    
    def validation(self):
        return self._validation(self.root, float('-inf'), float('inf'))
    
    def _validation(self, root, min_value, max_value):
        if root is None:
            return True
        if root.value < min_value or root.value >= max_value:
            return False
        left_check = self._validation(root.left, min_value, root.value)
        if left_check:
            right_check = self._validation(root.right, root.value, max_value)
            return right_check
        return False
    
    def delete(self, key):
        self.root = self._delete(key, self.root)
    
    def _delete(self, key, root):
        if root is None: # base case
            return None
        if key > root.value:
            root.right = self._delete(key, root.right)
        elif key < root.value:
            root.left = self._delete(key, root.left)
        else: # key == value
            # node is leaf
            if root.left is None and root.right is None:
                return None
            # node has at least 1 child
            else:
                # node has 1 child
                if root.right is None:
                    return root.left
                elif root.left is None:
                    return root.right
                else: 
                
                    root.value = self.findMax(root.left)
                    
                    root.left = self._delete(root.value, root.left)
        return root
    
    def findMax(self, root):
        current = root
        while current.right is not None:
            current = current.right
        return current.value
                

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(10)
    bst.insert(15)
    bst.insert(17)
    bst.insert(25)
    bst.insert(5)
    
    bst2 = BinarySearchTree()
    bst2.root = Node(10)
    bst2.root.left = Node(10)
    
    bst.inorder()
    print()
    print(bst.search(15))
    print(bst2.validation())
    
    bst.delete(22)
    bst.inorder()
    