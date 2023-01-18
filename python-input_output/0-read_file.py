#!/usr/bin/python3
def read_file(filename=""):
    """reading a textfile and print to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
