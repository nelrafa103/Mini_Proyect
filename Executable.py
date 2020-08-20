from Chess_Chips import play
from Chess_Board import letters_in_board
from Chess_Board import values_of_chips
from Chess_Chips import chips_on_game
boolean = True
play_1 = play()
count = 1
while boolean:
   try:
     count = count + 1
     print(count)
     play_1.case_1(count)
    
   except:
      print('Incorrect')
    # break
      continue
  