#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return None
    else:
        my_list2 = my_list.copy()
        my_list2.sort(reverse=True)
        return (my_list2[0])
