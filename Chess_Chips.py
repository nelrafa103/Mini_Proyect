from Chess_Board import Properies
from Chess_Board import Messages
from Chess_Board import LETTERS_IN_BOARD
from Chess_Board import VALUES_OF_THE_CHIPS
# This class contain all the movemets in the chips and attack

# messages.next_position()
# messages.next_position()


class ChipsOfGame(Properies):

    def Attack(self, eaten, attaker):
        self.Eat_In_Chess(eaten, attaker)

    def Movement_Front(self, value):
        self.value = value
        self.Walk_Horizontal(self.value)

    def Movement_To_Side(self, value):
        self.value = value
        self.Walk_Vertical(self.value)

    def Movement_Inline(self, value):
        self.value = value
        self.Walk_Horizontal(self.value)
        self.Walk_Vertical(self.value)

    def Movement_In_L(self, value_x, value_y):
        self.value_x = value_x
        self.value_y = value_y
        self.Walk_Horizontal(self.value_x)
        self.Walk_Vertical(self.value_y)


Chips_On_Game = ChipsOfGame(None,None,None)
