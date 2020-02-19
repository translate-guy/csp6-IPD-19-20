####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####


team_name = 'zero heroes' # Only 10 chars displayed.

strategy_name = 'round four'
strategy_description = 'betray 4 times after using collude facing betray'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
  betray = 0
  if my_history == 0:
    return 'c'
  if their_history == 'b'
    return 'b'
    betray += !
  elif betray %4 == 0:
    return 'c'
  else:
    return 'c'
