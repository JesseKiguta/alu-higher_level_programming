#!/usr/bin/python3
''' Specifies the size of the square '''


class Square:
    """ class defines the size of the square
    the square's size has to be a positive integer """
    def __init__(self, size=0):
        """ initializes attributes then
        uses if statements to raise errors when
        the size is not a positive integer """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
