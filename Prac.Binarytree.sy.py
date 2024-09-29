class Tree:
    # Constructor to initialize a tree node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Inorder traversal of the tree
    def Inorder(self, Root):
        if Root is None:
            return
        self.Inorder(Root.left)
        print(Root.value, end=' ')
        self.Inorder(Root.right)

    # Insert a new value in the BST
    def Insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.Insert(value)
        else:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.Insert(value)

    # Delete a node from the BST
    def Delete(self, parent, value):
        # Recursively find the node to delete
        if value < self.value:
            if self.left:
                self.left.Delete(self, value)
        elif value > self.value:
            if self.right:
                self.right.Delete(self, value)
        else:
            # Node to be deleted found
            # Case 1: Node with no children (leaf node)
            if self.left is None and self.right is None:
                if parent.left == self:
                    parent.left = None
                else:
                    parent.right = None
                del self

            # Case 2: Node with only one child (right child)
            elif self.left is None:
                if parent.left == self:
                    parent.left = self.right
                else:
                    parent.right = self.right
                del self

            # Case 2: Node with only one child (left child)
            elif self.right is None:
                if parent.left == self:
                    parent.left = self.left
                else:
                    parent.right = self.left
                del self

            # Case 3: Node with two children
            else:
                # Find the in-order successor (smallest in the right subtree)
                successor = self.right
                while successor.left is not None:
                    successor = successor.left
                # Replace value with successor value
                self.value = successor.value
                # Delete the successor
                self.right.Delete(self, successor.value)

# Driver code to demonstrate the Tree operations
if __name__ == "__main__":
    # Create the root of the tree
    Root = Tree(6)

    # Insert nodes into the tree
    Root.Insert(4)
    Root.Insert(2)
    Root.Insert(5)
    Root.Insert(9)
    Root.Insert(8)
    Root.Insert(10)

    # Print the Inorder traversal of the tree after insertion
    print("Inorder traversal after insertion:", end=' ')
    Root.Inorder(Root)
    print()  # Newline for better formatting

    # Delete a node from the tree and show the traversal
    Root.Delete(Root, 2)
    print("After deleting 2:", end=' ')
    Root.Inorder(Root)
    print()

    Root.Delete(Root, 4)
    print("After deleting 4:", end=' ')
    Root.Inorder(Root)
    print()

    Root.Delete(Root, 6)
    print("After deleting 6:", end=' ')
    Root.Inorder(Root)
    print()
