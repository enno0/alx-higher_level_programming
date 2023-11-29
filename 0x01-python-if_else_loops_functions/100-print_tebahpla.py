#!/usr/bin/python3
print("".join(f"{chr(ch) if ch % 2 == 0 else chr(ch - 32)}" for ch in reversed(range(97, 123))))
