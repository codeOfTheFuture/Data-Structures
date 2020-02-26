from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.current_nodes = None
        self.dll = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # If the key that is passed in is not in storage dict then return None
        if key not in self.storage:
            return None
        else:
            # Set the current node to be the tail of the dll
            current_node = self.dll.tail 

            # Check each node starting with the tail to see if the node value matches the key   
            while current_node.value is not key:

                # If the current node value does not match the key reassign current node to be
                # the previous node in the dll
                current_node = current_node.prev

            # Check to see if the current node is the tail.  If it is then it does not need to be moved
            # to the end of the dll
            if current_node is not self.dll.tail:
                self.dll.move_to_end(current_node)

            # Return the value of the key
            return self.storage[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:
            self.storage[key] = value
        elif self.current_nodes == self.limit:
            item = self.dll.remove_from_head()
            self.storage.pop(item, None)
            self.dll.add_to_tail(key)
            self.storage[key] = value
        else:
            self.dll.add_to_tail(key)
            self.storage[key] = value
            self.current_nodes = self.dll.length

