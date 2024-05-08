from fsm import MooreMachine, State, get_graph

pitch_count = MooreMachine('Pitch Count')
count_states = {(i, j) : State(f'{i}-{j}', initial=(i == 0 and j == 0)) for i in range(4) for j in range(3)}

accepting_states = {'Base': State('Base'), 'Out': State('Out')}
for key, state in count_states.items():
    balls, strikes = key
    state[r'HBP'] = accepting_states['Base']
    if balls < 3:
        state[r'Ball'] = count_states[(balls + 1, strikes)]
    else:
        state[r'Ball'] = accepting_states['Base']
    if (strikes < 2):
        state[r'Strike'] = count_states[(balls, strikes + 1)]
        state[r'Foul'] = count_states[(balls, strikes + 1)]
    else:
        state[r'Strike'] = accepting_states['Out']
        state[r'Foul'] = state
        
for state in accepting_states.values():
    state[r'New Batter'] = count_states[(0, 0)]

get_graph(pitch_count).draw('count.png', prog='dot')
    
