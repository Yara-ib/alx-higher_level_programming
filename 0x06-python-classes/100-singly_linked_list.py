#!/usr/bin/python3
class Node:
    """ Class for creating a node.

    Attributes:
        data: data @nodes.
        next_node: pointer/reference to the next node.

    Returns:
        a new node.
    """
    def __init__(self, data, next_node=None):
        """ Initializing the attributes for creating a node. """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Getting the data. """
        return self.data

    @data.setter
    def data(self, value):
        """ Setting the data. """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.data = value

    @property
    def next_node(self):
        """ Getting the next.node. """
        return self.next_node

    @next_node.setter
    def next_node(self, value):
        """ Setting the next.node. """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.next_node = value


class SinglyLinkedList:
    """ Class for creating SinglyLinkedList.

    Attributes:
        list: list to store the data @nodes.

    Returns:
        string using __str__
    """
    list = []

    def __init__(self):
        """ Initializing the attributes for creating a SinglyLinkedList. """
        self.head = None
        self.data = 0

    def sorted_insert(self, value):
        """ Inserting a new node in the SinglyLinkedList. """
        if self.head is None:
            self.head = Node.next_node
            Node.data = value
        else:
            while Node.next_node is None:
                Node.next_node = None
                Node.data = value
        SinglyLinkedList.list.append(value)

    def __str__(self) -> str:
        """ Converting the data stored @each node to string and sorting it."""
        return '\n'.join(map(str, sorted(SinglyLinkedList.list)))
