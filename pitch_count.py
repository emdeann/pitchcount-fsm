from fsm import MooreMachine, State

pitch_count = MooreMachine('Pitch Count')
balls = 0
strikes = 0
count_states = {(0, 0): State('0-0', initial=True), (0, 1): State('0-1'), (0, 2): State('0-2'), 
                (1, 1): State('1-1'), (1, 2): State('1-2'),
                (2, 0): State('2-0'), (2, 1): State('2-1'),
                (2, 2): State('2-2'), (3, 0): State('3-0'),
                (3, 1): State('3-1'), (3, 2): State('3-2')}
accepting_states = {'Base': State('Base'), 'Out': State('Out')}
