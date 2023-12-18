#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        undefined_variable
    except NameError as e:
        print(message)
        raise 
