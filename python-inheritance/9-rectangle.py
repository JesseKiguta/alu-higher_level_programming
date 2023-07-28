#!/usr/bin/python3
''' Full rectangle '''
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

    def area(self):
        ''' Calculates area 
        '''
        return self.__width * self.__height

    def __str__(self):
        ''' Returns info about the rectangle 
        '''
        return f"[Rectangle] {self.__width}/{self.__height}"
