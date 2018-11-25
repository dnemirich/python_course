# Task 8


class QueueNode:
    """ Node: Class for single node of LinkedQueue """

    def __init__(self, elem, nextnode):
        """ Initializes new node """
        self.element = elem
        self.next = nextnode


class QueueIterator:
    """ QueueIterator: Iterator for LinkedQueue """

    def __init__(self, node, emptynode):
        """ Initializes new Iterator """
        self.start = node
        self.stop = emptynode

    def __next__(self):
        """ Returns next element of queue: next(iter) """
        if self.start == self.stop:
            raise StopIteration
        else:
            current = self.start.element
            self.start = self.start.next
            return current
