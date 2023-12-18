#!/usr/bin/python3
def raise_exception():
    try:
        result = "string" + 42
    except TypeError as e:
        raise
