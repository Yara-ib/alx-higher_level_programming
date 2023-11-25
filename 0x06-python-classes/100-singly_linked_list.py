#!/usr/bin/python3
""" Creating a Singly linked list. """


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
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ Getting the data. """
        return self.__data

    @data.setter
    def data(self, value):
        """ Setting the data. """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Getting the next.node. """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Setting the next.node. """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ Class for creating SinglyLinkedList.

    Attributes:
        list: list to store the data @nodes.

    Returns:
        string using __str__
    """

    def __init__(self):
        """ Initializing the attributes for creating a SinglyLinkedList. """
        self.head = None
        self.list = []

    def sorted_insert(self, value):
        """ Inserting a new node in the SinglyLinkedList. """
        node = Node(value)

        if self.head is None:
            self.head = node
            node.data = value
            self.head.next_node = node.next_node = None

        else:
            ptr = self.head
            while ptr.next_node is not None:
                ptr = ptr.next_node
            ptr.next_node = node
            node.next_node = None
            node.data = value

        self.list.append(value)

    def __str__(self) -> str:
        """ Converting the data stored @each node to string and sorting it."""
        return '\n'.join(map(str, sorted(self.list)))
