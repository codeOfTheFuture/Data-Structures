# from dll_queue import Queue
# from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BinarySearchTree(value)
        current_node = self

        if current_node.value is None:
            current_node.value = value
        else:
            while True:
                if current_node.value > value:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = new_node
                        return
                else:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = new_node
                        return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current_node = self
        while True:
            if current_node.value is target:
                return True
            if current_node.value > target:
                if current_node.left is None:
                    return False
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    return False
                else: current_node = current_node.right

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while True:
            if current_node.right is None:
                return current_node.value
            else:
                current_node = current_node.right



    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
