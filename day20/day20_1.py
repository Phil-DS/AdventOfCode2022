from itertools import cycle
from data import data2 as data


max_size = len(data) -1

def swap(l, e):
    i = l.index(e)
    _,val = l.pop(i)
    iNew = (i+val)%len(l)
    if iNew == 0:
        l.append(e)
        return
    l.insert(iNew, e) 

def mix(arr):
    indexed_data = list(enumerate(data))
    for e in enumerate(data):
        swap(indexed_data, e)
    return [v for _,v in indexed_data]

moved_data = mix(data)
print(sum(moved_data[(i+moved_data.index(0))%(max_size+1)] for i in (1000, 2000, 3000)))
