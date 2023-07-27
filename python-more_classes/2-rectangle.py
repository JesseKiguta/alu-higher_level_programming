#!/usr/bin/python3
''' calculates the area and perimeter of a rectangle '''


class Rectangle:
    ''' defines the height and width of a rectangle '''
    def __init__(self, width=0, height=0):
        ''' initializes attrbutes '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' gets width using a private instance attribute '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' sets width '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' gets height using a private instance attribute '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' sets height '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' calculates the area '''
        return self.__height * self.__width

    def perimeter(self):
        ''' calculates the perimeter '''
        if self.__height or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
