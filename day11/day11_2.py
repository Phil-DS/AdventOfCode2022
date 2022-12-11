monkeys = {
    0:
    {
        'items': [57, 58],
        'Operation': lambda old: old * 19,
        'Test': lambda val:  2 if val % 7 == 0 else 3
    },

    1:
    {
        'items': [66, 52, 59, 79, 94, 73],
        'Operation': lambda old: old + 1,
        'Test': lambda val:  4 if val % 19 == 0 else 6
    },

    2:
    {
        'items': [80],
        'Operation': lambda old: old + 6,
        'Test': lambda val:  7 if val % 5 == 0 else 5
    },

    3:
    {
        'items': [82, 81, 68, 66, 71, 83, 75, 97],
        'Operation': lambda old: old + 5,
        'Test': lambda val:  5 if val % 11 == 0 else 2
    },

    4:
    {
        'items': [55, 52, 67, 70, 69, 94, 90],
        'Operation': lambda old: old * old,
        'Test': lambda val:  0 if val % 17 == 0 else 3
    },

    5:
    {
        'items': [69, 85, 89, 91],
        'Operation': lambda old: old + 7,
        'Test': lambda val:  1 if val % 13 == 0 else 7
    },

    6:
    {
        'items': [75, 53, 73, 52, 75],
        'Operation': lambda old: old * 7,
        'Test': lambda val:  0 if val % 2 == 0 else 4
    },

    7:
    {
        'items': [94, 60, 79],
        'Operation': lambda old: old + 2,
        'Test': lambda val:  1 if val % 3 == 0 else 6
    }
}

magicMod = 2*3*5*7*11*13*17*19


monkeyCounter = {
    0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0
}


def doMonkeyBusiness():
    for i in monkeys:
        while len(monkeys[i]['items']):
            currItem = monkeys[i]['items'].pop(0)
            newWorry = monkeys[i]['Operation'](currItem) % magicMod
            toMonkey = monkeys[i]['Test'](newWorry)
            monkeys[toMonkey]['items'].append(newWorry)
            monkeyCounter[i] += 1
            # print(currItem, i, '=>', toMonkey)


for round in range(10000):
    doMonkeyBusiness()


print(monkeyCounter)
top = list(sorted(monkeyCounter.values(),reverse = True))
print(top[0]*top[1])
# top = Object.values(monkeyCounter).sort((a, b) => b - a).slice(0, 2)
# console.log(top[0] * top[1])
