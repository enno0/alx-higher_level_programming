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
