#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(dic.keys())
    keys.sort()
    for i in keys:
        print("{}:{}".format(i, dic[i]))
