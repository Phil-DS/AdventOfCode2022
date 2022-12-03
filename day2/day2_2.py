from data import data

round_score = {
    'A': {
        'X': 3,
        'Y': 1,
        'Z': 2
    },
    'B': {
        'X': 1,
        'Y': 2,
        'Z': 3
    },
    'C': {
        'X': 2,
        'Y': 3,
        'Z': 1
    }
}

result_score = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

score = 0

for opp, result in data:
    score += result_score[result] + round_score[opp][result]

print(score)
