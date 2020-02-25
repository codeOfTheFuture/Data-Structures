import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        if self.len() == 0 :
            self.storage.add_to_head(value)
            self.storage.add_to_tail(value)
        else:
            self.storage.add_to_tail(value)
        
        self.size += 1
        return self.size
    def dequeue(self):
        if self.len() == 0:
            print('Stack is Empty')
            return None
        head = self.storage.head
        if self.storage.head == self.storage.tail:
            self.storage.head = None
        self.storage.remove_from_head()
        self.size -= 1
        return head.value
    def len(self):
        return self.size
