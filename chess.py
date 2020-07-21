import os
import turtle
try:
    boolean = True
    i = 0

    class message():
        def play(self):
            entry_1 = input("Enter the position of the chip you want to use")

        def next_position(self):
            entry_2 = input("Enter the next position for you chip")
    messages = message()

    def board(width, height):
        board_size = width * height
        return board_size

    messages.choose_color()
    while boolean:
        messages.play()

        class properies(object):
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

        class pawn(properies):
            @property
            def movements_pawn(self):
                self.walk_front(1)

            def attack_pawn(self, eaten, attaker):
                self.eat_in_chess(eaten, attaker)

        i += 1
        if i == 10:
            boolean = False

        class dame(properies):
            @property
            def movement_1(self):
                self.walk_front(messages.entry_3)

            def movement_2(self):
                self.walk_back(messages.entry_3)

            def movement_3(self):
                self.walk_left(messages.entry_3)

            def movement_4(self):
                self.walk_right(messages.entry_3)

            def movement_5(self):
                self.walk_right(messages.entry_3)
                self.walk_front(messages.entry_3)

            def movement_6(self):
                self.walk_left(messages.entry_3)
                self.walk_front(messages.entry_3)

            def attack_pawn(self, eaten, attaker):
                self.eat_in_chess(eaten, attaker)

        class bishop(properies):
            @property
            def movement_1(self):
                self.walk_right(messages.entry_3)
                self.walk_front(messages.entry_3)

            def movement_2(self):
                self.walk_left(messages.entry_3)
                self.walk_front(messages.entry_3)

            def attack_pawn(self, eaten, attaker):
                self.eat_in_chess(eaten, attaker)

        class tower(properies):
            def movement_1(self):
                self.walk_front(messages.entry_3)

            def movement_3(self):
                self.walk_left(messages.entry_3)

            def movement_4(self):
                self.walk_right(messages.entry_3)

except:
    print('It is not a correct value,debbung again.Please!')
    # class board:
    # def
