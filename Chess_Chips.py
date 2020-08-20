from Chess_Board import properies
from Chess_Board import auxiliar_class
# This class contain all the movemets in the chips and attack

# messages.next_position()
# messages.next_position()


class chips_of_game(properies):
    def attack(self, eaten, attaker):
        self.eat_in_chess(eaten, attaker)

    def update_chip_position(self, value, chip_type, color, new_value):
        self.color = color
        self.value = value
        self.new_value = new_value
        self.chip_type = chip_type
        counter = 0
        if self.position_x == messages.entry_1[0] and self.position_y == messages.entry_1[1]:
            for x in values_of_chips[self.color][self.chip_type]:
                if self.value == x:
                    values_of_chips[self.color][self.chip_type][counter] = self.new_value
                counter += 1


chips_on_game = chips_of_game(9, 9, 'red')


class play(auxiliar_class):
    def case_1(self, value_1):
        self.value_1 = value_1
        self.play()
        self.colors(self.value_1)
        print(self.color)
        self.search_of_chips(self.entry_1)
        print(self.chip_position)
        self.next_position()
        self.auxiliar_function()
        self.cop_1 = int(self.chip_position[0])
        self.cop_2 = self.chip_position[1]
        print(self.cop_2)
        print(self.count)
        print(self.bulma)

playes = play()
playes.case_1(1)
#  self.rules_for_chips(self.cop_1,self.count,self.cop_2,letters_in_board)
