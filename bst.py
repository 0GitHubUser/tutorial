class BST_Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_branch(self, data):
        if data == self.data:
            return
        elif data < self.data:
            if self.left is None:
                self.left = BST_Node(data)
            else:
                self.left.add_branch(data)
        else:
            if self.right is None:
                self.right = BST_Node(data)
            else:
                self.right.add_branch(data)

    def find_val(self, fval):
        if fval < self.data:
            if self.left is None:
                return 'Not Found'
            return self.left.find_val(fval)
        elif fval > self.data:
            if self.right is None:
                return 'Note Found'
            return self.right.find_val(fval)
        else:
            return 'data found'

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
            
        return self

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    

def build_tree(elements):
    root = BST_Node(elements[0])

    for i in range(1, len(elements)):
        root.add_branch(elements[i])
    return root       

if __name__ == '__main__':
    numbers = [22, 56, 89, 4, 67, 9, 78, 90, 14, 69]
    numbers_tree = build_tree(numbers)
    # print(numbers_tree.in_order_traversal())
    print(numbers_tree.find_val(78))
    print(numbers_tree.find_min())
    print(numbers_tree.delete(89))
    








            

