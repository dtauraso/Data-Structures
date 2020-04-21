import sys
sys.path.append('./doubly_linked_list')
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
        # dict = {key : value}  value is the node
        self.storage = DoublyLinkedList()
        self.quick_access = {}
        # pass

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        
        # if key in self.storage:
        #     self.storage[key].
        # else:
        # if the key exists
            # move_to_end(node)
                # pull the key from front()
                # insert it into end

            # return node.value
        # if the key doesn't exist
            # return None

        # (key, value) has just been acessed so must be moved to the end
        if key in self.quick_access:
            # doesn't moving the item require a new link from the dict?
            self.storage.move_to_end(self.quick_access[key])
            self.quick_access[key] = self.storage.tail

            return self.quick_access[key].value
        else:
            return None
        # pass

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

        # if the key is new (its considered the most reciently used item)
            # append it at the end
            # if no room
                # replace old node with new value
        # pass

        if key not in self.quick_access:
            
            # if there is room
            if len(self.storage) < self.limit:
                # append it at the end
                self.storage.add_to_tail(value)
                self.quick_access[key] = self.storage.tail
            else:
                # no roomt so erase the last item and append it at end
                self.storage.delete(self.storage.tail)

                self.storage.add_to_tail(value)
                self.quick_access[key] = self.storage.tail
        else:
            # key already exists so move it from it's old location to the end
            # while updating the value
            self.storage.delete(self.quick_access[key])
            self.storage.add_to_tail(value)
            self.quick_access[key] = self.storage.tail

        # if key is already in the cache
            # if not already at the end
                # take it and move it to the end
    def Print(self):
        print()
        {print(i, self.quick_access[i].value) for i in self.quick_access}