#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """
    Defines a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a given size and position.

        Args:
            size (int, optional): The size of the square. Default is 0.
            position (tuple, optional): The position of the square. Default is (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size to be set.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self._position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The position to be set.

        Raises:
            TypeError: If the provided position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' in stdout.
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Converts the square to a string.

        Returns:
            str: The string representation of the square.
        """
        result = ""
        if self.size == 0:
            result += "\n"
        else:
            result += "\n" * self.position[1]
            result += "\n".join(" " * self.position[0] + "#" * self.size for _ in range(self.size))
        return result
