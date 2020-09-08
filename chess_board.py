import os

letters_in_board = {'A': 1, 'B': 2, 'C': 3,
                    'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,"I": 9}

values_of_chips = {'black': {'pawns':  [[2, 'A'], [2, 'B'], [2, 'C'], [2, 'D'], [2, 'E'], [2, 'F'], [2, 'G'], [2, 'H']], 'bishops':  [[1, 'C'], [1, 'F']], 'towers':  [[1, 'A'], [1, 'H']], 'horses':  [[1, 'B'], [2, 'G']], 'king':  [[1, 'E']], 'dame': [[1, 'D']]},

                   'white': {'pawns':  [[7, 'A'], [7, 'B'], [7, 'C'],  [7, 'D'],  [7, 'E'],  [7, 'F'],  [7, 'G'], [7, 'H']], 'bishops':  [[8, 'C'],  [8, 'F']], 'towers':  [[8, 'A'],  [8, 'H']], 'horses':   [[8, 'B'],  [8, 'G']], 'king':  [[8, 'E']], 'dame':  [[8, 'D']]}}


class Message():
    def play(self):
        self.entry_1 = input(
            "Enter the position of the chip you want to use:  ")

        if self.entry_1 == "status":
            auxiliar.status()

    def next_position(self):
        self.entry_2 = input("Enter the next position for you chip:  ")

        if self.entry_2 == "status":
            auxiliar.status()


messages = Message()


class Properies(object):
    def __init__(self, position_x, position_y, color):
        self.position_x = position_x
        self.position_y = position_y
        self.color = color


class Rules(Message):

    def colors(self, counter):
        self.counter = counter
        if self.counter % 2 != 0:
            self.color = 'white'
        else:
            self.color = 'black'

    def search_of_chips(self, intro_value):
        self.intro_value = intro_value
        self.t = 0
        if int(self.entry_1[0]) in range(1, 9) and self.entry_1[1] in letters_in_board:
            for x in values_of_chips[self.color]:
                self.t = 0
                for y in values_of_chips[self.color][x]:
                    if y[0] == int(self.intro_value[0]) and y[1] == self.intro_value[1]:
                        self.chip_position = y
                        self.chip_type = x
                        print(self.chip_type)
                        return True
                    else:
                        self.t += 1
        return False

    def rules_for_chips(self, value_1, value_2):
        self.value_1, self.value_2 = value_1, value_2
        if letters_in_board[self.entry_2[1]] - letters_in_board[self.entry_1[1]] < 0:
         self.decorative = -1
        else:
         self.decorative = 1
        #Begin with logic
        print( (letters_in_board[self.entry_2[1]] - letters_in_board[self.entry_1[1]]) )
        print(self.chip_type)
        if int(self.entry_2[0]) in range(1, 9) and self.entry_2[1] in letters_in_board:
            if int(self.entry_1[0]) != int(self.entry_2[0]) or letters_in_board[self.entry_1[1]] != letters_in_board[self.entry_2[1]]:
                if (self.chip_type == "towers" and int(self.entry_1[0]) != int(self.entry_2[1]) and letters_in_board[self.entry_1[1]] != letters_in_board[self.entry_2[1]]):
                    print("N1")
                    return 
                if (self.chip_type == "bishops" and (int(self.entry_2[0]) - int(self.entry_1[0])) * self.addition != (letters_in_board[self.entry_2[1]] - letters_in_board[self.entry_1[1]]) * self.decorative):
                  print("N2")
                  return
                if self.chip_type != "horses" and int(self.entry_1[0]) != int(self.entry_2[0]) and letters_in_board[self.entry_1[1]] != letters_in_board[self.entry_2[1]] and (int(self.entry_2[0]) - int(self.entry_1[0])) * self.addition != (letters_in_board[self.entry_2[1]] - letters_in_board[self.entry_1[1]]) * self.decorative:
                    print("Case 4: wrote")
                    return 

                if self.chip_type == "horses" and ((int(self.entry_2[0]) - int(self.entry_1[0])) * self.addition) + (letters_in_board[self.entry_2[1]] - letters_in_board[self.entry_1[1]]) * self.decorative == 3:
                    if (letters_in_board[self.entry_2[1]] - letters_in_board[self.entry_1[1]]) * self.decorative >= 3 or (int(self.entry_2[0]) - int(self.entry_1[0])) * self.decorative >= 3:
                       print("Case 6: Wrote")
                       return 
                elif self.chip_type == "horses":
                    print("Case 5:  Wrote")
                    return 


                if int(self.entry_2[0]) in range(int(self.value_1[0]), int(self.value_2[0]), self.addition_2) and letters_in_board[self.entry_2[1]] in range(letters_in_board[self.value_1[1]], self.value_2[1]):
                    print("OK")
                    return True
                else:
                    print("It is not a correct movemnt. Try again: 1")
                    return 
            else:
                print('It is not a correct movemnt. Try again: 2')
                return 

    def movements_chips(self):
        if self.chip_type == 'pawns':
            self.value_range = [self.chip_position[0] +
                                self.count, letters_in_board[self.entry_2[1]] + 1]

        elif self.chip_type == 'king':
            self.value_range = [self.chip_position[0] +
                                self.count, letters_in_board[self.entry_2[1]] + self.count]

        else:
            self.value_range = [9, letters_in_board["I"]]

    def dont_eat_your_team(self, values):
        self.values = values
        if self.search_of_chips(self.values) == True:
            return False

    def auxiliar_function(self):

        if self.color == 'black':
            self.addition = 1
            self.addition_2 = 1
            self.count = 2
        else:
            self.addition = -1
            self.addition_2 = 1
            if self.chip_type == "pawns" or self.chip_type == "king":
                self.addition_2 = -1
            self.count = -2

    """def dont_go_through_tiles(self):
        if self.chip_type != "horses":
            self.clone = list(self.entry_1)
            self.clone[0] = int(self.clone[0])
            for x in values_of_chips[self.color]:
                for y in values_of_chips[self.color][x]:
                    if y[0] in range(int(self.entry_1[0]), int(self.entry_2[0]), self.addition) or letters_in_board[y[1]] in range(letters_in_board[self.entry_1[1]], self.entry_2[1]) and y != self.clone:
                        print("you cant do that", y, x,
                              self.value_2, self.value_1)
                        return False
"""
    def finish_game(self):
        self.colors(self.counter + 1)
        if values_of_chips[self.color]["king"][0] == [None, None]:
            print("The game had finish")


rule = Rules()


class AuxiliarClass(Rules):
    def operating_system(self):
        if self.counter % 2 == 0:
            if os.name == "posix":
                os.system('clear')
            else:
                os.system('cls')

    def status(self):
        print(values_of_chips)
        print("Revision")


auxiliar = AuxiliarClass()