from data import data


type_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

round_score = {
    'A': {
        'X': 3,
        'Y': 6,
        'Z': 0
    },
    'B': {
        'X': 0,
        'Y': 3,
        'Z': 6
    },
    'C': {
        'X': 6,
        'Y': 0,
        'Z': 3
    }
}

score = 0

for opp, me in data:
    score += type_score[me] + round_score[opp][me]

print(score)
