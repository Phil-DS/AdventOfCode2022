from data import state, moves

for count, col_from, col_to in moves:
    state[col_to] = state[col_from][:count] + state[col_to]
    state[col_from] = state[col_from][count:]

print(''.join(state[i][0] for i in state))
