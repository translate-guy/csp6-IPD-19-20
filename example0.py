####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E0'
strategy_name = 'you dont wanna betray me'
strategy_description = 'Collude until betrayed. If betrayed, betray for the rest.'
    
def move(my_history, their_history, my_score, their_score):
  '''collude until facing betray and betray for the rest'''

  if my_history == 0:
    return 'c'  
  elif 'b' in their_history:
    return 'b'
  else:
    return 'c'
    