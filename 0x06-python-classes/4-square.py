#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Class constructor with optional size parameter"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Property getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Public instance method to calculate and return the area"""
        return self.__size ** 2
