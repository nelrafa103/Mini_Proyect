from Chess_Board import Rules_
from Chess_Board import Messages
from Chess_Board import LETTERS_IN_BOARD
from Chess_Board import VALUES_OF_THE_CHIPS
from Chess_Chips import Chips_On_Game
#Movements = ChipsOfGame()
#Actions = {'Pawns': ChipsOfGame.Movement_Front()}
boolean = True
while boolean:
 try:
  Rules_.Counter()
  Messages.Play()
  Messages.Next_Position()
 except:
  Messages.Next_Position()


