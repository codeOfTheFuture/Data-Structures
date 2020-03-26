from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()


    def push(self, value):
        if self.len() == 0:
            self.storage.add_to_head(value)
        else:
            self.storage.add_to_head(value)

        self.size += 1
        return self.size


    def pop(self):
        if self.len() == 0:
            return None
        else :
            self.size -= 1
            return self.storage.remove_from_head()


    def len(self): 
        return self.size


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        if self.len() == 0 :
            self.storage.add_to_tail(value)
        else:
            self.storage.add_to_tail(value)
        
        self.size += 1
        return self.size
    def dequeue(self):
        if self.len() == 0:
            print('Stack is Empty')
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()
        

        
    def len(self):
        return self.size


######################################################################

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
        if self.left and self.right:
            cb(self.value)
            self.left.for_each(cb)
            self.right.for_each(cb)
        elif self.left and not self.right:
            cb(self.value)
            self.left.for_each(cb)
        elif self.right and not self.left:
            cb(self.value)
            self.right.for_each(cb)
        else:
            cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    queue = Queue()
    def bft_print(self, node):
        self.queue.enqueue(node)

        while self.queue.len():
            node = self.queue.dequeue()

            print(node.value)

            if node.left:
                self.queue.enqueue(node.left)
            if node.right:
                self.queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    new_stack = Stack()
    def dft_print(self, node):
        self.new_stack.push(node)

        while self.new_stack.len():
            node = self.new_stack.pop()

            print(node.value)

            if node.left:
                self.new_stack.push(node.left)
            if node.right:
                self.new_stack.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)
