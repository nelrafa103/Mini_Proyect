from Chess_Board import rules
from Chess_Board import messages
from Chess_Board import letters_in_board
from Chess_Board import values_of_chips
from Chess_Chips import chips_on_game
from Chess_Board import rule
from Chess_Chips import actions
boolean = True
count = 0
while boolean:
    try:
      print('correct')
    
    except:
     messages.next_position()
     print('Incorrect')
 