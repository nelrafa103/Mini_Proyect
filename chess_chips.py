from chess_board import Chips
from chess_board import auxiliar
from chess_board import messages
from chess_board import values_of_chips
from chess_board import board
from chess_board import letters_in_board
# This class contain all the movemets in the chips and attack


   
class Play():
 def play_case_1(self, value_1):
     self.value_1 = value_1
     board.colors(self.value_1)
     messages.play()   
     board.search_of_chips(messages.entry_1)
     chips = Chips(
        board.chip_position[0], board.chip_position[1], board.color, board.chip_type)
     messages.next_position()
     auxiliar.postives_numbers()
     chips.movements()
     chips.dont_go_through_tiles()
     board.update_chip_position(messages.entry_2)
     chips.eating()
     board.finish_game()
     auxiliar.operating_system()
players = Play()