import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Modifying the order of elements is O(1) time, because they are not stored strictly in a sequence .

        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        
        pass

    def dequeue(self):
        pass

    def len(self):
        pass
