#!/usr/bin/python3
""" Specifies the size of the square """


class Square:
    ''' class defines the size of the square with parameters '''
    def __init__(self, size=0):
        ''' initializes attributes '''
        if type(size) is not int:
            ''' ensures size is an integer '''
            raise TypeError("size must be an integer")
        ''' returns an error message if not an integer '''
        if size <= 0:
            ''' ensures size is positive '''
            raise ValueError("size must be >= 0")
        ''' returns an error if negative '''
        else:
            ''' changes default size to new size '''
            self.__size = size
