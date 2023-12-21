#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Class constructor with optional size and position parameters"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Property getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter for position"""
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method to calculate and return\
              the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method to print the square with # characters \
        and positional spaces"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
