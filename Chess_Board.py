import os

letters_in_board = {'A': 1, 'B': 2, 'C': 3,
                    'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}

values_of_chips = {'black': {'pawns':  [[2, 'A'], [2, 'B'], [2, 'C'], [2, 'D'], [2, 'E'], [2, 'F'], [2, 'G'], [2, 'H']], 'bishops':  [[1, 'C'], [1, 'F']], 'towers':  [[1, 'A'], [1, 'H']], 'horses':  [[1, 'B'], [2, 'G']], 'king':  [[1, 'E']], 'dame': [[1, 'D']]},

                   'white': {'pawns':  [[7, 'A'], [7, 'B'], [7, 'C'],  [7, 'D'],  [7, 'E'],  [7, 'F'],  [7, 'G'], [7, 'H']], 'bishops':  [[8, 'C'],  [8, 'F']], 'towers':  [[8, 'A'],  [8, 'H']], 'horses':   [[8, 'B'],  [8, 'G']], 'king':  [[8, 'E']], 'dame':  [[8, 'D']]}}


class message():
    def play(self):
        self.entry_1 = input("Enter the position of the chip you want to use:  ")

    def next_position(self):
        self.entry_2 = input("Enter the next position for you chip:  ")

messages = message()


class properies(object):
    def __init__(self, position_x, position_y, color):
        self.position_x = position_x
        self.position_y = position_y
        self.color = color

    def walk_horizontal(self, value):
        self.value = value
        self.position_x = self.value + 1

    def walk_vertical(self, value):
        self.value = value
        self.position_y = letters_in_board[self.value[1]]

    def remove_from_board(self):
        self.position_x = None
        self.position_y = None

    def eat_in_chess(self, eaten, attaker):
        self.eaten = eaten
        self.attaker = attaker
        if self.attaker.position_x == self.eaten.position_x and self.attaker.position_y == self.eaten.position_y:
            eaten.remove_from_board()


class rules():

    def rules_of_eat(self, entry):
        self.entry = entry
        if int(self.entry[0]) * values_of_chips[self.entry[1]] > 64:
            messages.next_position()
    # def Search_Of_Chips(self,value):

    def colors(self, counter):
        self.counter = counter
        if self.counter % 2 != 0:
            self.color = 'white'
        else:
            self.color = 'black'

    def search_of_chips(self):
        for x in values_of_chips[self.color]:
            for y in values_of_chips[self.color][x]:
                if y[0] == int(messages.entry_1[0]) and y[1] == messages.entry_1[1]:
                    self.chip_position = y
                    self.chip_type = x
                    return 'Its ok'
        else:
            return 'It is not ok'


rule = rules()