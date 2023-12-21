#!/usr/bin/python3
"""This module defines a node class."""


class Node:
    """
    Defines a node of a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The reference to the next node in the linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node with the given data and next_node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the data for the node.

        Args:
            value (int): The data to be set.

        Raises:
            TypeError: If the provided data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Retrieves the reference to the next node.

        Returns:
            Node: The next node in the linked list.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the reference to the next node.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If the provided next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list.

    Attributes:
        head (Node): The head of the linked list.
    """
    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Converts the linked list to a string.

        Returns:
            str: The string representation of the linked list.
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next_node
        return "\n".join(map(str, result))
