#!/usr/bin/python3
def no_c(my_string):
    my_string2 = ""
    for char in my_string:
        if char.lower() != 'c' and char.upper() != 'C':
            my_string2 = my_string2 + char
    return my_string2
