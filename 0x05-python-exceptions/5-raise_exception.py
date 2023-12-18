#!/usr/bin/python3
def raise_exception():
    try:
        result = "string" + 42
    except TypeError as e:
        print(f"Type Error: {e}")
        raise
