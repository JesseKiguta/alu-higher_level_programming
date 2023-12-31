#!/usr/bin/python3
''' square number one '''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Square class '''
    def __init__(self, size):
        ''' Initializes attributes
        '''
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        ''' Calculates the area
        '''
        return self.__size ** 2
