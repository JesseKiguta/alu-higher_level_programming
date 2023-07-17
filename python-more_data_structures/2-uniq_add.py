#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set()
    for num in my_list:
        unique_list.add(num)
    unique_sum = sum(unique_list)
    return unique_sum
