from chess_board import Properies
from chess_board import messages
# This class contain all the movemets in the chips and attack

# messages.next_position()
# messages.next_position()
LETTERS_IN_BOARD = {'A': 1, 'B': 2, 'C': 3,
                    'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
VALUES_OF_THE_CHIPS = {'Black': {'Pawn_1': [2, 'A'], 'Pawn_2': [2, 'B'], 'Pawn_3': [2, 'C'], 'Pawn_4': [2, 'D'], 'Pawn_5': [2, 'E'], 'Pawn_6': [2, 'F'], 'Pawn_7': [2, 'G'], 'Pawn_8': [2, 'H']},
  
                       'White': {'Pawn_1': [7, 'A'], 'Pawn_2': [7, 'B'], 'Pawn_3': [7, 'C'], 'Pawn_4': [7, 'D'], 'Pawn_5': [7, 'E'], 'Pawn_6': [7, 'F'], 'Pawn_7': [7, 'G'], 'Pawn_8': [7, 'H']}}

       

class ChipsOfGame(Properies):

    def attack(self, eaten, attaker):
        self.eat_in_chess(eaten, attaker)

    def movement_front(self, value):
        self.value = value
        self.walk_horizontal(self.value)

    def movement_right(self, value):
        self.value = value
        self.walk_vertical(self.value)

    def movement_inline_right(self, value):
        self.value = value
        self.walk_horizontal(self.value)
        self.walk_vertical(self.value)


# VALUES_OF_THE_CHIPS = {'Black':Firts2.movement_front}
# print(VALUES_OF_THE_CHIPS['Black'])
Rules_ = ChipsOfGame(14, VALUES_OF_THE_CHIPS['Black']['Pawn_1'][1], 'White')
print(Rules_.position_x)
messages.next_position()
Rules_.movement_front(messages.entry_2)
# Rules_.movement_inline_right(messages.entry_2)
#Rules_.movement_front(Rules_.i + 1)
print(Rules_.position_y, Rules_.position_x)
