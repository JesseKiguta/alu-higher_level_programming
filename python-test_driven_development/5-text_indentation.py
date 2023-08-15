#!/usr/bin/python3
''' Text indentation '''


def text_indentation(text):
    '''Prints a text with 2 new lines after . ? and :'''
    if type(text) is not str:
        raise TypeError("text must be a string")

    special_char_encountered = False

    for char in text:
        if char not in ['.', '?', ':']:
            print(char, end="")
            special_char_encountered = False
        else:
            print(char)
            special_char_encountered = True
    if special_char_encountered:
        print()
