#!/usr/bin/python3
''' Calculating the area of a square '''


class Square:
    """ this class defines size as a positive integer and
    computes the area of a square """
    def __init__(self, size=0):
        """ defines size as
        positive and
        an integer """
        if type(size) is not int:
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ calculates the area using
        a mathematical formula """
        return self.__size ** 2
