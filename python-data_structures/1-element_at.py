#!/usr/bin/python3
def element_at(my_list, idx):
    idx = my_list.index()
    if idx < 0 or idx > len(my_list):
        return None
    else:
        print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
