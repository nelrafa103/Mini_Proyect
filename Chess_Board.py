import os

LETTERS_IN_BOARD = {'A': 1, 'B': 2, 'C': 3,
                    'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}

VALUES_OF_THE_CHIPS = {'Black': {'Pawns':  [[2, 'A'], [2, 'B'], [2, 'C'], [2, 'D'], [2, 'E'], [2, 'F'], [2, 'G'], [2, 'H']] , 'Bishops':  [[1, 'C'], [1, 'F']] , 'Towers':  [[1, 'A'],[1, 'H']] , 'Horses':  [[1, 'B'], [2, 'G']] , 'King':  [[1, 'E']] , 'Dame': [[1, 'D']] },

                       'White': {'Pawns':  [[7, 'A'], [7, 'B'], [7, 'C'],  [7, 'D'],  [7, 'E'],  [7, 'F'],  [7, 'G'], [7, 'H']] , 'Bishops':  [[8, 'C'],  [8, 'F']] , 'Towers':  [ [8, 'A'],  [8, 'H']] , 'Horses':   [[8, 'B'],  [8, 'G']] , 'King':  [ [8, 'E']] , 'Dame':  [[8, 'D']]}}


class Message():
    def Play(self):
        self.entry_1 = input("Enter the position of the chip you want to use")

    def Next_Position(self):
        self.entry_2 = input("Enter the next position for you chip:  ")
       # self.entry_3 = input()


Messages = Message()


class Properies(object):
    def __init__(self, position_x, position_y, color):
        self.position_x = position_x
        self.position_y = position_y
        self.color = color

    def Walk_Horizontal(self, value=None):
        self.value = value
        self.position_x = int(self.value[0])

    def Walk_Vertical(self, value=None):
        self.value = value
        self.position_y = LETTERS_IN_BOARD[self.value[1]]

    def Remove_From_Board(self):
        self.position_x = None
        self.position_y = None

    def Eat_In_Chess(self, eaten, attaker):
        self.eaten = eaten
        self.attaker = attaker
        if self.attaker.position_x == self.eaten.position_x and self.attaker.position_y == self.eaten.position_y:
            eaten.remove_from_board()
# messages.Next_Position()


class Rules():
    counter = 0
    colors = str()
    def Counter(self):
        self.counter += 1

    def Rules_Of_Eat(self, entry):
        self.entry = entry
        if int(self.entry[0]) * VALUES_OF_THE_CHIPS[self.entry[1]] > 64:
            Messages.Next_Position()
    #def Search_Of_Chips(self,value):
    def Colors(self):
     if counter % 2 != 0:
      colors = 'White'
     else:
      colors = 'Black'
Rules_ = Rules()