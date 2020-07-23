import os
import turtle


class Message():
        def play(self):
            entry_1 = input("Enter the position of the chip you want to use")

        def next_position(self):
            entry_2 = input("Enter the next position for you chip")
messages = Message()

class Properies(object):
            def __init__(self, position_x, position_y, color):
                self.position_x = position_x
                self.position_y = position_y
                self.color = color

            def remove_from_board(self):
                self.position_x = None
                self.position_y = None

            def walk_front(self, value):
                self.value = value
                self.position_y += self.value

            def walk_back(self, value):
                self.value = value
                self.position_y -= self.value

            def walk_left(self, value):
                self.value = value
                self.position_x -= self.value

            def walk_right(self, value):
                self.value = value
                self.position_x += self.value

            def eat_in_chess(self, eaten, attaker):
                self.eaten = eaten
                self.attaker = attaker
                if self.attaker.position_x == self.eaten.position_x:
                    eaten.remove_from_board()

print('It is not a correct value,debbung again.Please!')
