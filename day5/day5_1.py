from data import state, moves

for count, col_from, col_to in moves:
    for i in range(count):
        state[col_to] = [state[col_from].pop(0)] + state[col_to]

print(''.join(state[i][0] for i in state))
