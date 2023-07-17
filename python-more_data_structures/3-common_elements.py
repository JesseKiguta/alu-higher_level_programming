#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = set()
    set_3 = set_1 + set_2
    for elements in set_3:
        if elements in set_1 and elements in set_2:
            common_set.add(elements)
    return common_set
