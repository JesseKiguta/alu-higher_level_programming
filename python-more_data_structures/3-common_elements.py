#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = set()
    for elements in set_1:
        for elements in set_2:
            common_set.add(elements)
    return common_set
