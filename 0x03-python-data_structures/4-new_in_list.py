#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len1 = len(my_list)
    my_list2 = list(my_list)
    if idx < 0:
        return my_list
    elif idx > len1-1:
        return my_list
    else:
        my_list2[idx] = element
        return my_list2
