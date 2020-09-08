from chess_board import Properies
from chess_board import AuxiliarClass
from chess_board import messages
from chess_board import values_of_chips
# This class contain all the movemets in the chips and attack


class ChipsOfGame(AuxiliarClass):
    def attack(self, eaten, extra_count):
        self.eaten = eaten
        self.extra_count = extra_count
        self.colors(self.extra_count)
        if self.search_of_chips(self.eaten) == True:
            values_of_chips[self.color][self.chip_type][self.t] = [None, None]

    def update_chip_position(self, new_value):
        self.new_value = new_value
        self.search_of_chips(self.new_value)
        values_of_chips[self.color][self.chip_type][self.t -
                                                    1][0], values_of_chips[self.color][self.chip_type][self.t - 1][1] = int(self.new_value[0]), self.new_value[1]
    # i dont know how to named

    def calleds(self):
        if self.chip_type == "pawns" or self.chip_type == "king":
            return self.rules_for_chips(self.entry_1, self.value_range)
        else:
            return self.rules_for_chips([1,"A"],self.value_range)
#chips_on_game = chips_of_game(9, 9, 'red')

#This class contain the default procedement

class Play(ChipsOfGame):
    def case_1(self, value_1):
     
        self.value_1 = value_1
        self.play()
        self.colors(self.value_1)
        self.search_of_chips(self.entry_1)
        self.next_position()
        self.dont_eat_your_team(self.entry_2)
        self.auxiliar_function()
        self.movements_chips()
     #   self.dont_go_through_tiles()
        if self.calleds() == True:
            self.update_chip_position(self.entry_2)
            self.finish_game()
        else:
          return 1 + "hola"
