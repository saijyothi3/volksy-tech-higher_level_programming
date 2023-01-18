#!/usr/bin/python3
"""writing string to a text file"""


def write_file(filename="", text=""):
    """string to text file"""
    with open(filename, mode="w", encoding="UTF8") as f:
        return filename.wite(text)
