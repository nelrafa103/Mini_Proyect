from chess_board import Properies
from chess_board import AuxiliarClass
from chess_board import messages
from chess_board import values_of_chips
# This class contain all the movemets in the chips and attack


class ChipsOfGame(AuxiliarClass):

    def update_chip_position(self, new_value):
        self.new_value = new_value
        self.colors(self.counter - 1)
        self.search_of_chips(self.entry_1)
        print(self.color,self.indicator,self.color)
        values_of_chips[self.color][self.chip_type][self.indicator 
                                                    ][0], values_of_chips[self.color][self.chip_type][self.indicator][1] = int(self.new_value[0]), self.new_value[1]
    # i dont know how to named

    def calleds(self):
        if self.chip_type == "pawns" or self.chip_type == "king":
            return self.rules_for_chips(self.entry_1, self.value_range)
        else:
            return self.rules_for_chips([1,"A"],self.value_range)
#This class contain the default procedement

class Play(ChipsOfGame):
    def play_case_1(self, value_1):
     
        self.value_1 = value_1
        self.play()
        self.colors(self.value_1)
        self.search_of_chips(self.entry_1)
        self.next_position()
        self.auxiliar_function() 
        self.movements_chips()
        self.postives_numbers()
        self.dont_go_through_tiles()
        if self.calleds() == True and self.dont_eat_your_team() == True:
            self.update_chip_position(self.entry_2)
            self.finish_game()
        else:
         print(values_of_chips)
