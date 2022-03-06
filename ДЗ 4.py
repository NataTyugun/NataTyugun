import math,statistics
def my_log(lst: list) -> list:
    l = []
    for i in len(lst):
        if lst[i]>0 :
            l[i] = math.log(lst[i])
        else :
            l[i] = None
    return l

