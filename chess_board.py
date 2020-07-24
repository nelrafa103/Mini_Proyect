import os


class Message():
    def play(self):
        self.entry_1 = input("Enter the position of the chip you want to use")

    def next_position(self):
        self.entry_2 = input("Enter the next position for you chip")
        self.entry_3 = input()


messages = Message()


class Properies(object):
    def __init__(self, position_x, position_y, color):
        self.position_x = position_x
        self.position_y = position_y
        self.color = color

    def walk_horizontal(self, value=None):
        self.value = value
        self.position_x = self.value[0]

    def walk_vertical(self, value=None):
        self.value = value
        self.position_y = self.value[1]

    def remove_from_board(self):
        self.position_x = None
        self.position_y = None

    def eat_in_chess(self, eaten, attaker):
        self.eaten = eaten
        self.attaker = attaker
        if self.attaker.position_x == self.eaten.position_x and self.attaker.position_y == self.eaten.position_y:
            eaten.remove_from_board()
# messages.next_position()
