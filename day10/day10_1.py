from data import data

x = 1
cycle = 1
nextCheck = 20
checkFreq = 40

checkVals = []

for inst, val in data:
    match inst:
        case 'noop':
            cycle += 1
        case 'addx':
            cycle += 1
            if cycle >= nextCheck:
                checkVals.append(x*nextCheck)
                nextCheck += checkFreq
            cycle += 1
            x += val
    if cycle >= nextCheck:
        checkVals.append(x*nextCheck)
        nextCheck += checkFreq


print(sum(checkVals))

