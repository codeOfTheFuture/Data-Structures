import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        if self.len() == 0:
            self.storage.add_to_head(value)
            self.storage.add_to_tail(value)
            print(self.storage)
        else:
            self.storage.add_to_head(value)
            print(self.storage)

        self.size += 1
        return self.size
    def pop(self):
        if self.len() == 0:
            print('Stack is Empty')
            return
        head = self.storage.head
        if self.storage.head == self.storage.tail:
            self.storage.tail = None
        self.storage.remove_from_head()
        self.size -= 1
        return head.value
    def len(self): 
        return self.size
