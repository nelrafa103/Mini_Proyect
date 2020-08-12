from Chess_Board import properies
from Chess_Board import messages
from Chess_Board import letters_in_board
from Chess_Board import values_of_chips
from Chess_Board import rule
# This class contain all the movemets in the chips and attack

# messages.next_position()
# messages.next_position()


class chips_of_game(properies):

    def attack(self, eaten, attaker):
        self.eat_in_chess(eaten, attaker)

    def movement_front(self, value):
        self.value = value
        self.walk_horizontal(self.value)

    def movement_to_side(self, value):
        self.value = value
        self.walk_vertical(self.value)

    def movement_inline(self, value):
        self.value = value
        self.walk_horizontal(self.value)
        self.walk_vertical(self.value)

    def movement_in_l(self, value_x, value_y):
        self.value_x = value_x
        self.value_y = value_y
        self.walk_horizontal(self.value_x)
        self.walk_vertical(self.value_y)

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
messages.play()
messages.next_position()
rule.colors(1)
rule.search_of_chips()
rule.search_of_chips()
chips_on_game = chips_of_game(rule.chip_position[0], rule.chip_position[1], rule.color)
actions = {'pawns': chips_on_game.movement_front(int(chips_on_game.position_x))}
actions[rule.chip_type]
my_list = [chips_on_game.position_x,chips_on_game.position_y]
chips_on_game.update_chip_position(rule.chip_position,rule.chip_type,rule.color,my_list)
print(values_of_chips)
print('Mi vida')