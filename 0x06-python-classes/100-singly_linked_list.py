#!/usr/bin/python3
"""Class defining a node of a singly linked list
Singly linked list node
"""


class Node:
    """Node class
    Definition of the Node class
    data setter and getter methods,
    next_node setter and getter methods
    """
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node


class SinglyLinkedList:
    """Actual Singly linked List
        Now let's define methods for creating the list
    """

    def __init__(self):
        self.__head = None

    def __str__(self):
        current = self.__head
        result = ""
        while current is not None:
            if current.next_node is not None:
                result += str(current.data) + "\n"
            else:
                result += str(current.data)
            current = current.next_node
        return result

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self.__head:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node and current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
