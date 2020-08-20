import os

letters_in_board = {'A': 1, 'B': 2, 'C': 3,
                    'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}

values_of_chips = {'black': {'pawns':  [[2, 'A'], [2, 'B'], [2, 'C'], [2, 'D'], [2, 'E'], [2, 'F'], [2, 'G'], [2, 'H']], 'bishops':  [[1, 'C'], [1, 'F']], 'towers':  [[1, 'A'], [1, 'H']], 'horses':  [[1, 'B'], [2, 'G']], 'king':  [[1, 'E']], 'dame': [[1, 'D']]},

                   'white': {'pawns':  [[7, 'A'], [7, 'B'], [7, 'C'],  [7, 'D'],  [7, 'E'],  [7, 'F'],  [7, 'G'], [7, 'H']], 'bishops':  [[8, 'C'],  [8, 'F']], 'towers':  [[8, 'A'],  [8, 'H']], 'horses':   [[8, 'B'],  [8, 'G']], 'king':  [[8, 'E']], 'dame':  [[8, 'D']]}}


class message():
    def play(self):
        self.entry_1 = input(
            "Enter the position of the chip you want to use:  ")

    def next_position(self):
        self.entry_2 = input("Enter the next position for you chip:  ")


messages = message()


class properies(object):
    def __init__(self, position_x, position_y, color):
        self.position_x = position_x
        self.position_y = position_y
        self.color = color

    def remove_from_board(self):
        self.position_x = None
        self.position_y = None

    def eat_in_chess(self, eaten, attaker):
        self.eaten = eaten
        self.attaker = attaker
        if self.attaker.position_x == self.eaten.position_x and self.attaker.position_y == self.eaten.position_y:
            eaten.remove_from_board()


class rules(message):

    def rules_of_eat(self, entry):
        self.entry = entry
        if int(self.entry[0]) * values_of_chips[self.entry[1]] > 64:
            messages.next_position()

    def colors(self, counter):
        self.counter = counter
        if self.counter % 2 != 0:
            self.color = 'white'
        else:
            self.color = 'black'

    def search_of_chips(self, intro_value):
        self.bulma = range(0, 10)
        self.intro_value = intro_value
        for x in values_of_chips[self.color]:
            for y in values_of_chips[self.color][x]:
                if y[0] == int(self.intro_value[0]) and y[1] == self.intro_value[1]:
                    self.chip_position = y
                    self.chip_type = x
                    return 'Its ok'
        else:
            return 'It is not ok'

    def rules_for_chips(self, value_x_i, value_x_l, value_y_i, value_y_l):
        if value_x_i in value_x_l and value_y_i in value_x_l:
            return 'Yes!'
        else:
            return 'No!'

    def movements_chips(self):
        if self.chip_type == 'pawns' or 'king':
            value = range(self.chip_position[0], auxiliar.count)

        elif self.chip_type != 'pawns' or rule.chip_type != 'king':
            value = range(0, 8)

    def dont_eat_your_team(self, values):
        self.values = values
        self.search_of_chips(self.values)


rule = rules


class auxiliar_class(rule):
    def operating_system(self):
        if os.name == "posix":
            os.system('clear')
        else:
            os.system('cls')

    def auxiliar_function(self):
        if self.color == 'black':
            self.count = self.chip_position[0] + 1
        else:
            self.count = self.chip_position[0] - 1


auxiliar = auxiliar_class
