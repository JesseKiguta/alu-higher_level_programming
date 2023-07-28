#!/usr/bin/python3
''' inheritance with lists '''

class MyList(list):
    ''' MyList inherits from mylist '''
    def print_sorted(self):
        ''' Prints the list sorted in ascending order '''
        print(sorted(self, reverse=False))
