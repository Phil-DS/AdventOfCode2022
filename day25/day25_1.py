from data import data
import math

digitLUT = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

def SNAFU(value):
    finalVal = 0
    for i,c in enumerate(reversed(value)):
        finalVal += digitLUT[c]*(5**i)
    return finalVal

def reverseSNAFU(value):
    qchars = []
    max5 = math.ceil(math.log(value,5))
    curr = value
    for i in range(max5,-1,-1):
        pos = curr // (5**i)
        curr -= pos * (5**i)
        qchars.append(pos)
    
    chars = []
    carry = 0
    for q in reversed(qchars):
        q += carry
        carry = 0
        if q <= 2:
            chars.append(str(q))
            continue
        carry = 1
        if q == 3:
            chars.append('=')
        elif q == 4:
            chars.append('-')
        else:
            chars.append('0')

        
    chars.reverse()
    if chars[0] == '0':
        chars.pop(0)

    return ''.join(chars)

print(reverseSNAFU(314159265))

l = list(map(SNAFU,data))

print(reverseSNAFU(sum(map(SNAFU,data))))