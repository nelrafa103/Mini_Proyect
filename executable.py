from chess_chips import Play
from chess_board import letters_in_board
from chess_board import values_of_chips
import turtle

boolean = True
play_1 = Play()
count = 1
while boolean:
  try:
     play_1.case_1(count)
     count += 1
     print("It is ok")
  except:
      continue
#