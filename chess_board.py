import os

letters_in_board = {'A': 1, 'B': 2, 'C': 3,
                    'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, "I": 9}

values_of_chips = {'black': {'pawns':  [[2, 'A'], [2, 'B'], [2, 'C'], [2, 'D'], [2, 'E'], [2, 'F'], [2, 'G'], [2, 'H']], 'bishops':  [[1, 'C'], [1, 'F']], 'towers':  [[1, 'A'], [1, 'H']], 'horses':  [[1, 'B'], [2, 'G']], 'king':  [[1, 'E']], 'dame': [[1, 'D']]},

                   'white': {'pawns':  [[7, 'A'], [7, 'B'], [7, 'C'],  [7, 'D'],  [7, 'E'],  [7, 'F'],  [7, 'G'], [7, 'H']], 'bishops':  [[8, 'C'],  [8, 'F']], 'towers':  [[8, 'A'],  [8, 'H']], 'horses':   [[8, 'B'],  [8, 'G']], 'king':  [[8, 'E']], 'dame':  [[8, 'D']]}}

class Message():

    def status(self):
        print(values_of_chips)
        print("Revision")

    def play(self):
        #print('It is your turn, ' + board.color)
        self.entry_1 = input(
            "Enter the position of the chip you want to use:  ")

        if self.entry_1 == "status":
            self.status()

    def next_position(self):
        self.entry_2 = input("Enter the next position for you chip:  ")

        if self.entry_2 == "status":
            self.status()

    def error_case_1(self):
        print("You cant do this")
        return 'error' + 1 

messages = Message()


class Characteristics(object):
    def __init__(self, position_x, position_y, color, types):
        self.position_x = position_x
        self.position_y = position_y
        self.color = color
        self.type = types


class Board():

    def colors(self, counter):
        self.counter = counter
        if self.counter % 2 != 0:
            self.color = 'white'
        else:
            self.color = 'black'

    def search_of_chips(self, intro_value):
        self.intro_value = intro_value
        self.indicator = 0
        if int(messages.entry_1[0]) in range(1, 9) and messages.entry_1[1] in letters_in_board:
            for x in values_of_chips[self.color]:
                self.indicator = 0
                for y in values_of_chips[self.color][x]:
                    if y[0] == int(self.intro_value[0]) and y[1] == self.intro_value[1]:
                        self.chip_position = y
                        self.chip_type = x
                        return True
                    else:
                        self.indicator += 1
        else:
         return messages.error_case_1(),

    def finish_game(self):
        self.colors(self.counter + 1)
        if values_of_chips[self.color]["king"][0] == [None, None]:
            print("The game had finish")
            return False

    def dont_eat_your_team(self):
        if self.search_of_chips(messages.entry_2) == True and messages.entry_1[0] != messages.entry_2[0] and messages.entry_1[1] != messages.entry_2[1]:
            return messages.error_case_1()
        else:
            return True

    def update_chip_position(self, new_value):
         self.new_value = new_value
         self.colors(self.counter - 1)
         self.search_of_chips(messages.entry_1)
         values_of_chips[self.color][self.chip_type][self.indicator
                                                    ][0], values_of_chips[self.color][self.chip_type][self.indicator][1] = int(self.new_value[0]), self.new_value[1]

    
board = Board()


class Chips(Characteristics):
    def attack(self):
        board.colors(board.counter + 1)
        if board.search_of_chips(messages.entry_2) == True:
            return True

    def auxiliar_function(self):

        if board.color == 'black':
            self.addition = 1
            self.addition_2 = 1
            self.count = 2
        else:
            self.addition = -1
            self.addition_2 = 1
            if board.chip_type == "pawns" or board.chip_type == "king":
                self.addition_2 = -1
            self.count = -2

    def rules_for_movements(self, value_1, value_2):
        self.value_1, self.value_2 = value_1, value_2
        self.result = self.attack()
        if int(messages.entry_2[0]) in range(1, 9) and messages.entry_2[1] in letters_in_board or messages.entry_2[1] == "I":
            if int(messages.entry_1[0]) != int(messages.entry_2[0]) or letters_in_board[messages.entry_1[1]] != letters_in_board[messages.entry_2[1]]:
                if self.type == "towers" and messages.entry_1[0] != messages.entry_2[0] and messages.entry_1[1] != messages.entry_2[1]:
                    return  messages.error_case_1()
                if self.type == "bishops" and (int(messages.entry_2[0]) - int(messages.entry_1[0])) * auxiliar.case_1 != (letters_in_board[messages.entry_2[1]] - letters_in_board[messages.entry_1[1]]) * auxiliar.case_2:
            
                    return  messages.error_case_1()
                if self.type != "horses" and int(messages.entry_1[0]) != int(messages.entry_2[0]) and letters_in_board[messages.entry_1[1]] != letters_in_board[messages.entry_2[1]] and (int(messages.entry_2[0]) - int(messages.entry_1[0])) * auxiliar.case_1 != (letters_in_board[messages.entry_2[1]] - letters_in_board[messages.entry_1[1]]) * auxiliar.case_2:
                  
                    return  messages.error_case_1()
                if self.type == "horses" and ((int(messages.entry_2[0]) - int(messages.entry_1[0])) * auxiliar.case_1) + (letters_in_board[messages.entry_2[1]] - letters_in_board[messages.entry_1[1]]) * auxiliar.case_2 == 3:
                    if (letters_in_board[messages.entry_2[1]] - letters_in_board[messages.entry_1[1]]) * auxiliar.case_2 >= 3 or (int(messages.entry_2[0]) - int(messages.entry_1[0])) * auxiliar.case_1 >= 3:
                        return  messages.error_case_1()
                elif self.type == "horses":
                    return  messages.error_case_1()
                if self.type == 'pawns' and (int(messages.entry_2[0]) - int(messages.entry_1[0])) * auxiliar.case_1 == (letters_in_board[messages.entry_2[1]] - letters_in_board[messages.entry_1[1]]) * auxiliar.case_2 and self.result == True:
                    if (letters_in_board[messages.entry_2[1]] - letters_in_board[messages.entry_1[1]]) * auxiliar.case_2 == 1 and (int(messages.entry_2[0]) - int(messages.entry_1[0])) * auxiliar.case_1 == 1:
                        return True
                if int(messages.entry_2[0]) in range(int(self.value_1[0]), int(self.value_2[0]), self.addition_2) and letters_in_board[messages.entry_2[1]] in range(letters_in_board[self.value_1[1]], self.value_2[1]):
                    return True
                else:
                
                    return messages.error_case_1()
            else:
                return  messages.error_case_1()

    def movements_chips(self):
        if self.type == 'pawns':
            self.value_range = [self.position_x +
                                self.count, letters_in_board[messages.entry_1[1]] + 1]

        elif self.type == 'king':
            self.value_range = [self.position_x +
                                self.count, letters_in_board[messages.entry_2[1]] + self.count]

        else:
            self.value_range = [9, letters_in_board["I"]]

    def movements(self):
        self.auxiliar_function()
        self.movements_chips()
        auxiliar.postives_numbers()
        board.dont_eat_your_team()
        if self.type == "pawns" or self.type == "king":
            return self.rules_for_movements(messages.entry_1, self.value_range)
        else:
            return self.rules_for_movements([1, "A"], self.value_range)

    def eating(self):
        if self.result == True:
            values_of_chips[board.color][self.type][board.indicator] = [
                None, None]

    def dont_go_through_tiles(self):
        self.clone = list(messages.entry_1)
        self.clone[0] = int(self.clone[0])
        if self.type != "horses":
            for x in values_of_chips[self.color]:
                for y in values_of_chips[self.color][x]:
                    if y[0] in range(int(messages.entry_1[0]), int(messages.entry_2[0]) + auxiliar.add_1, self.addition) and letters_in_board[y[1]] in range(letters_in_board[messages.entry_1[1]], letters_in_board[messages.entry_2[1]] + auxiliar.add_2) and self.clone != y:
                        return  messages.error_case_1()
        return True


class AuxiliarClass():
    def operating_system(self):
        if board.counter % 5 == 0:
            if os.name == "posix":
                os.system('clear')
            else:
                os.system('cls')

    def postives_numbers(self):
        if (int(messages.entry_2[0]) - int(messages.entry_1[0])) < 0:
            self.case_1 = -1
        else:
            self.case_1 = 1
        if letters_in_board[messages.entry_2[1]] - letters_in_board[messages.entry_1[1]] < 0:
            self.case_2 = -1
        else:
            self.case_2 = 1

        if messages.entry_1[0] == messages.entry_2[0]:
            self.add_1 = 1
        else:
            self.add_1 = 0
        if messages.entry_1[1] == messages.entry_2[1]:
            self.add_2 = 1
        else:
            self.add_2 = 0


auxiliar = AuxiliarClass()
