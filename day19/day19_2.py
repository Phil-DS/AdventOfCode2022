from multiprocessing import Pool
import random
from data import data

def run(blueprint, cycles):
    initial_robot_state = [1,0,0,0]
    initial_resourse_state = [0,0,0,0]

    ore, clay, obsidian, geode = blueprint

    def alter_resources(delta):
        for i in range(len(initial_resourse_state)):
            initial_resourse_state[i] -= delta[i]

    for i in range(cycles):
        delta_robot_state = [0,0,0,0]
        if all(cost <= res for cost,res in zip(geode,initial_resourse_state)):
            alter_resources(geode)
            delta_robot_state[3] += 1

        elif all(cost <= res for cost,res in zip(obsidian,initial_resourse_state)):
            alter_resources(obsidian)
            delta_robot_state[2] += 1
        
        elif all(cost <= res for cost,res in zip(clay,initial_resourse_state)) and random.random()> .5:
            alter_resources(clay)
            delta_robot_state[1] += 1

        elif all(cost <= res for cost,res in zip(ore,initial_resourse_state)) and random.random()> .5:
            alter_resources(ore)
            delta_robot_state[0] += 1
        
        alter_resources([-1 * s for s in initial_robot_state])
        initial_robot_state = [a+b for a,b in zip(delta_robot_state, initial_robot_state)]
    
    return initial_resourse_state

f = 1
for k in [1,2,3]:
    g = 0
    v = data[k]
    for i in range(10000):   
        score = run(v,32)[3]
        if score > g:
            g = score
    print(g)
    f *= g
print(f)