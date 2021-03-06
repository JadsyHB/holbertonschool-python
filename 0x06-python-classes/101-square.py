#!/usr/bin/python3
"""
Module 101-square
Defines Square class with private attribute, size validation and area
accessible with setters and getters and a printer and position
"""


class Square:
    """
    class Square definition

    Args:
        size: size of side of square, default size is 0
        position: current position

    Functions:
        __init__(self, size, position)
        size(self)
        size(self, value)
        area(self)
        my_print(self)
        position(self)
        position(self, value)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initilization of square

        Attributes:
            size: size of side of square, default value is 0
            position: position with default 0, 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        Args:
            value: size is set to value when value is an int
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter
        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter

        Args:
            value: sets the position to the tuple in value
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates are of a square

        Returns:
              area
        """
        return (self.__size)**2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))

    def __str__(self):
        """
        String representation like my_print()
        """
        string = ""
        if self.__size == 0:
            return string

        string += "\n" * self.position[1]
        string += "\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)])
        return string
