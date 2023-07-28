#!/usr/bin/python3
''' Rectangle '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' New Rectangle class inherits from BaseGeometry, and represents a
    rectangle '''
    def __init__(self, width, height):
        ''' Initializes attributes
        '''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
