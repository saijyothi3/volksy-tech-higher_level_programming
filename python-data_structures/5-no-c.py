#!/usr/bin/python3
def no_c(my_string):
    my_string = "Calcutta"
    for x in my_string:
        if x != 'c' and x != 'C':
            return my_string
        new_string = []
        new_string.append(x)
        return("".join(new_string))
