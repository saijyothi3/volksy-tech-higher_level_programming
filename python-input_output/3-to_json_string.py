#!/usr/bin/python3
"""module returns the JSON representation of object"""


import json


def to_json_string(my_obj):
    """returning object"""
    return json.dumps(my_obj)
