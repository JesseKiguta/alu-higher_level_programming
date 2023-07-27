#!/usr/bin/python3
''' compare rectangles '''


class Rectangle:
    ''' defines a rectangle '''
    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        ''' initializes attributes '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        ''' prints rectangle with the # '''
        ch = ""
        if self.__width == 0 or self.__height == 0:
            return ch
        for i in range(self.__height):
            for j in range(self.__width):
                ch += str(self.print_symbol)
            ch += '\n'
        return ch[:-1]

    def __repr__(self):
        ''' returns a string similar to code of generating new object '''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        ''' deletes the rectangle while printing a message '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' returns the biggest rectangle based on the area '''
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
