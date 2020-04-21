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
        # dict = {key : {key: value}}  {key: value} is the node
        self.storage = DoublyLinkedList()
        self.quick_access = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    # oldest    ->     newest
    def get(self, key):
        
        # (key, value) has just been acessed so must be moved to the end
        if key in self.quick_access:
            self.storage.move_to_end(self.quick_access[key])
            # update the link to ensure we are pointing to the right node
            self.quick_access[key] = self.storage.tail

            return self.quick_access[key].value['value']
        else:
            return None

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

    # oldest    ->     newest
    def set(self, key, value):

        if key not in self.quick_access:
            
            # if there is room
            if len(self.storage) < self.limit:
                # append it at the end
                self.storage.add_to_tail({'key': key, 'value': value})
                self.quick_access[key] = self.storage.tail
            else:
                # print('no room')
                # no room so erase the first item and append it at end
                del self.quick_access[self.storage.head.value['key']]

                self.storage.delete(self.storage.head)

                self.storage.add_to_tail({'key': key, 'value': value})
                self.quick_access[key] = self.storage.tail
        else:
            # key already exists so move it from it's old location to the end
            # while updating the value

            self.storage.delete(self.quick_access[key])

            self.storage.add_to_tail({'key': key, 'value': value})
            self.quick_access[key] = self.storage.tail

    def Print(self):
        print()
        print('quick access')
        {print(i, self.quick_access[i].value) for i in self.quick_access}
        print('order')
        tracker = self.storage.head
        while tracker:
            print(tracker.value)
            tracker = tracker.next