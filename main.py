# Set up all coin states
from itertools import product
import copy
coin = ['H', 'T']
num_square = 16
coin_values = ()
all_states = coin
for i in range(0, num_square):
    coin_values = coin_values + (i,)

for i in range(0, num_square - 1):
    states = list(product(all_states, coin))
    all_states = []
    for state in states:
        all_states.append(tuple([item for sublist in state for item in sublist]))
#all_states = list(product(coin, coin, coin, coin))

# flip function
def flip(coin):
    if coin == 'H':
        return 'T'
    else:
        return 'H'

# set up the permutations
results = {}
assignments = {}
for state in all_states:
    results[state] = []
    assignments[state] = -1
    for index in range(0, len(state)):
        new_state = list(copy.deepcopy(state))
        new_state[index] = flip(new_state[index])
        results[state].append([tuple(new_state), -1])

candidates = [copy.deepcopy(assignments)]
final_candidate = {}
complete = False
while (len(candidates) > 0):
    candidate = candidates.pop()
    for index, (key, value) in enumerate(candidate.items()):
        added = False
        if value == -1:
            for index2 in range(0, num_square):
                new_candidate = copy.deepcopy(candidate)
                opposite_key = []
                for e in key:
                    opposite_key.append(flip(e))
                new_candidate[key] = index2
                new_candidate[tuple(opposite_key)] = index2

                # check if this assignment make sense
                duplicate = False
                not_fully_done = False
                for result in results.items():
                    unique_values = set()
                    for spot in result[1]:
                        coin = new_candidate[spot[0]]
                        if coin != -1:
                            if coin in unique_values:
                                duplicate = True
                            else:
                                unique_values.add(coin)
                        else:
                            not_fully_done = True

                if not duplicate:
                    if not_fully_done:
                        candidates.append(new_candidate)
                        added = True
                    else:
                        for (k, v) in new_candidate.items():
                            print(k, v)
                        final_candidate = new_candidate
                        complete = True
                        break

        if added:
            break

        if complete:
            break
    if complete:
        break

# Verification
for result in results.items():
    unique_values = set()
    for spot in result[1]:
        coin = final_candidate[spot[0]]
        spot[1] = coin
        if coin != -1:
            if coin in unique_values:
                print("duplicate found")

# for result in results.items():
#     print(result)

        
        

