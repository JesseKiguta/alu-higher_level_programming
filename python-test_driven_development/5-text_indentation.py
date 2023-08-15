#!/usr/bin/python3
''' 
Text indentation 
'''


def text_indentation(text):
    '''
    Prints a text with 2 new lines after . ? and :
    '''
    if type(text) is not str:
        raise TypeError("text must be a string")

    new = ""
    substring = ""
    temp = [] * 2
    flag = 0

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if i < len(text) and text[i] == '.' or text[i] == '?'
           or text[i] == ':':
            if flag == 0:
                temp = text.split(text[i], 1)
                flag = 1
            else:
                temp = substring.split(text[i], 1)
            new += temp[0].lstrip(' ') + text[i]
            substring = temp[1]
            print("{:s}".format(new))
            print()
            new = ""
    if flag == 0:
        text = text.lstrip(' ')
        text = text.rstrip(' ')
        print("{:s}".format(text), end="")
    else:
        substring = substring.lstrip(' ')
        substring = substring.rstrip(' ')
        print("{:s}".format(substring), end="")
