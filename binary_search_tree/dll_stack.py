from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()


    def push(self, value):
        if self.len() == 0:
            self.storage.add_to_head(value)
            print(self.storage)
        else:
            self.storage.add_to_head(value)
            print(self.storage)

        self.size += 1
        return self.size


    def pop(self):
        if self.len() == 0:
            print('Stack is Empty')
            return None
        else :
            self.size -= 1
            return self.storage.remove_from_head()


    def len(self): 
        return self.size