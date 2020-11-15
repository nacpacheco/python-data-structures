class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.value)

class BinarySearchTree():

    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return self.root
        else:
            current_node = self.root
            while (True):
                if new_node.value < current_node.value:
                    if not current_node.left:
                        current_node.left = new_node
                        print('inserted ' + str(new_node) + ' to the left of ' + str(current_node))
                        return self
                    current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = new_node
                        print('inserted ' + str(new_node) + ' to the right of ' + str(current_node))
                        return self
                    current_node = current_node.right


    def remove(self,value):
        if self.root == None:
            return False
        current_node = self.root
        parent_node = None
        while (current_node):
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif value == current_node.value:
                # Match!

                # No right child
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                    else:
                        # If parent > current, make current left child
                        # a child of parent
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.left
                
                # Right child with no left child
                elif current_node.right.left == None:
                    current_node.right.left = current_node.left
                    if parent_node == None:
                        self.root = current_node.right
                    else:
                        # if parent > current, make right child of left parent
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right
                
                # Right child has a left child
                else:
                    #find the right child's left most child
                    left_most = current_node.right.left
                    left_most_parent = current_node.right
                    
                    while (left_most.left != None):
                        left_most_parent = left_most
                        left_most = left_most.left
                    
                    # Parent's left subtree is now leftmost's right subtree
                    left_most_parent.left = left_most.right
                    left_most.left = current_node.left
                    left_most.right = current_node.right

                    if parent_node == None:
                        self.root = left_most
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = left_most
                        elif current_node.value > parent_node.value:
                            parent_node.right = left_most
                return True
        return False


    def lookup(self,value):
        if self.root == None:
            return False
        current_node = self.root
        while (current_node != None):
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False


    def breadth_first_search(self):
        current_node = self.root
        array = []
        
        # keeps track of the level, can get big if the tree is wide
        queue = []
        queue.append(current_node)
        while (queue):
            # Equivalent to shift, returns and remove first item
            current_node = queue[0]
            queue = queue[1:]
            array.append(current_node.value)
            # At each node from current level puts on queue left and right child
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return array

    def breadth_first_search_recursive(self, queue, array):
        if not queue:
            return array
        current_node = queue[0]
        queue = queue[1:]
        array.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        return self.breadth_first_search_recursive(queue, array)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        output = []
        self.inOrder(root, output)
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True

    def inOrder(self, root, output):
        if root is None:
            return
        
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)
        


def transverse(node):
    tree = Node(node.value)
    if node.left == None:
        tree.left = None
    else:
        tree.left = transverse(node.left)
    if node.right == None:
        tree.right = None
    else:
        tree.right = transverse(node.right)
    
    return tree

bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
print(bst.breadth_first_search())
print(bst.breadth_first_search_recursive(queue=[bst.root],array=[]))

# //     9
# //  4     20
# //1  6  15  170 