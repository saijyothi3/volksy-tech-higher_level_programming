#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    myList = []
    for i in my_list:
        if i % 2 == 0:
            myList.append(True)
        else:
            myList.append(False)
    return(myList)   
