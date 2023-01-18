#!/usr/bin/python3
"""appends to text file"""


def append_write(filename="", text=""):
    """function appends to a text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
