from data import data

import itertools

test_data = [
([1,1,3,1,1],
[1,1,5,1,1]),

([[1],[2,3,4]],
[[1],4]),

([9],
[[8,7,6]]),

([[4,4],4,4],
[[4,4],4,4,4]),

([7,7,7,7],
[7,7,7]),

([],
[3]),

([[[]]],
[[]]),

([1,[2,[3,[4,[5,6,7]]]],8,9],
[1,[2,[3,[4,[5,6,0]]]],8,9]),
]

def check_packets(l,r):
    for _l,_r in itertools.zip_longest(l,r,fillvalue=None):
        match _l,_r:
            case None, _:
                return True
            case _, None:
                return False
            case int(), int():
                if _l > _r:
                    return False
                if _l < _r:
                    return True
                continue
            case list(), int():
                _r = [_r]
                return check_packets(_l,_r)
            case int(), list():
                _l = [_l]
                return check_packets(_l,_r)
        
        c = check_packets(_l,_r)
        if c is not None:
            return c

    return None

count = 0

for i,p in enumerate(data):
    a,b = p
    # print('',a,'\n',b)
    print(i,check_packets(a,b))
    # print('#'*80)
    if check_packets(a,b):
        count += i+1
        

print(count)

