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
