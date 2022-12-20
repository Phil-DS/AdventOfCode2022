from itertools import cycle
from data import data2 as data

max_size = len(data) -1

def swap(arr, e):
    i = arr.index(e)
    _,val = arr.pop(i)
    new_ind = (i+val)%len(arr)
    if new_ind == 0:
        arr.append(e)
        return
    arr.insert(new_ind, e) 

def mix(arr,n):

    indexed_data = list(enumerate(arr))
    for _ in range(n):
        for e in enumerate(arr):
            swap(indexed_data, e)
    return [v for _,v in indexed_data]

new_data = [d*811589153 for d in data]
moved_data = mix(new_data,10)
print(sum(moved_data[(i+moved_data.index(0))%(max_size+1)] for i in (1000, 2000, 3000)))
