import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return f'{self.value}\n'
    # Insert the given value into the tree
    def insert(self, value):
        if self is None:
            return BinarySearchTree(value)
        # if the value is equal insert on the left
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if self:
        #     print(self.value, target)
        if self is None:
            return False
          
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

        elif target > self.value:
            # print('here')
            if self.right:
                return self.right.contains(target)
            else:
                return False

        elif target == self.value:
            return True
        # pass

    # Return the maximum value found in the tree
    def get_max(self):

        node = self
        max_ = 0
        if node:
            max_ = node.value

        my_stack = Stack()

        while my_stack.len() > 0 or node:
            # top = my_stack.pop()
            if node:
                my_stack.push(node)
                node = node.left
            else:
                node = my_stack.pop()
                # print(node.value)
                if(node.value > max_):
                    max_ = node.value
                node = node.right
        return max_
        # pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        node = self

        my_stack = Stack()

        while my_stack.len() > 0 or node:
            # top = my_stack.pop()
            if node:
                my_stack.push(node)
                node = node.left
            else:
                node = my_stack.pop()
                cb(node.value)
                node = node.right
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        if not node:
            return
        if node:
            in_order_print(node.left)
            print(node)
            in_order_print(node.right)


        # pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        # node is the tracker
        my_stack = Stack()

        while my_stack.len() > 0 or node:
            # top = my_stack.pop()
            if node:
                my_stack.push(node)
                node = node.left
            else:
                node = my_stack.pop()
                print(node)
                node = node.right

        # pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# x = BinarySearchTree(5)

# x.insert(6)
# tracker = x
# x.dft_print(tracker)

# print('here')
