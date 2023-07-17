#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list2 = []
    for number in my_list:
        list2.append(number % 2 == 0)
    return list2
