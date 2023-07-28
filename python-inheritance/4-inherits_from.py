#!/usr/bin/python3
''' Only sub class of '''


def inherits_from(obj, a_class):
    '''Checks if obj is an instance of a class that
    inherits directly/indirectly from a_class
    '''
    return issubclass(type(obj), a_class) and type(obj) != a_class
