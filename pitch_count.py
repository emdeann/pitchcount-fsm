from fsm import MooreMachine, State

pitch_count = MooreMachine('Pitch Count')
balls = 0
strikes = 0
count_states = {(0, 0): State('0-0', initial=True), (0, 1): State('0-1'), (0, 2): State('0-2'), 
                (1, 0): State('1-0'), (1, 1): State('1-1'), (1, 2): State('1-2'),
                (2, 0): State('2-0'), (2, 1): State('2-1'),
                (2, 2): State('2-2'), (3, 0): State('3-0'),
                (3, 1): State('3-1'), (3, 2): State('3-2')}

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
    
