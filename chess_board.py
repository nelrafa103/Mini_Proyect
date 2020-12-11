import os

letters_in_board = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
}

all_positions_of_pieces = {
    "black": {
        "pawns": [
            [2, "A"],
            [2, "B"],
            [2, "C"],
            [2, "D"],
            [2, "E"],
            [2, "F"],
            [2, "G"],
            [2, "H"],
        ],
        "bishops": [[1, "C"], [1, "F"]],
        "towers": [[1, "A"], [1, "H"]],
        "horses": [[1, "B"], [1, "G"]],
        "king": [[1, "E"]],
        "dame": [[1, "D"]],
    },
    "white": {
        "pawns": [
            [7, "A"],
            [7, "B"],
            [7, "C"],
            [7, "D"],
            [7, "E"],
            [7, "F"],
            [7, "G"],
            [7, "H"],
        ],
        "bishops": [[8, "C"], [8, "F"]],
        "towers": [[8, "A"], [8, "H"]],
        "horses": [[8, "B"], [8, "G"]],
        "king": [[8, "E"]],
        "dame": [[8, "D"]],
    },
}


class Properies(object):
    def __init__(self, position, color, piece_types):
        self.pieces_position = position
        self.color = color
        self.piece_types = piece_types


class Message:

    # All the thing with relation with the terminal

    def operating_system(self):

        if self.counter % 2 == 0:
            if os.name == "posix":
                os.system("clear")
            else:
                os.system("cls")

    def play(self):
        self.entry_1 = input("Enter the position of the chip you want to use:  ")
        try:
            if self.entry_1 == "status":
                print(all_positions_of_pieces)
            if (
                int(self.entry_1[0]) > 8
                or int(self.entry_1[0]) < 1
                or len(self.entry_1) != 2
                or self.entry_1[1] not in letters_in_board
            ):
                print("Try better this time ")
                return self.play()
            else:
                return True
        except:
            return self.play()

    def next_position(self):
        self.entry_2 = input("Enter the next position for you chip:  ")
        try:
            if self.entry_2 == "status":
                print(all_positions_of_pieces)
            if (
                int(self.entry_2[0]) > 8
                or int(self.entry_2[0]) < 1
                or len(self.entry_2) != 2
                or self.entry_2[1] not in letters_in_board
            ):
                print("Try better this time ")
                return self.next_position()
            else:
                return True
        except:
            return self.next_position()

    def menu(self):
        self.play()
        self.next_position()


messages = Message()
# messages.menu()


class Board:
    def converter_to_list(self, entry_1, entry_2):
        self.entry_1, self.entry_2 = entry_1, entry_2
        self.actual_position = [int(self.entry_1[0]), self.entry_1[1]]
        self.next_position = [int(self.entry_2[0]), self.entry_2[1]]
        return self.next_position

    def colors(self, counter):
        self.counter = counter
        if self.counter % 2 != 0:
            self.color = "white"
        else:
            self.color = "black"

    def search_of_pieces(self, intro_value, where_to_search, piece_color):
        self.index_position = 0
        self.intro_value, self.indicator, self.where_to_search, self.piece_color = (
            intro_value,
            0,
            where_to_search,
            piece_color,
        )
        for piece_type in where_to_search[self.piece_color]:
            self.indicator = 0
            for y in where_to_search[self.piece_color][piece_type]:
                if y[0] == self.intro_value[0] and y[1] == self.intro_value[1]:
                    self.piece_position, self.pieces_type = intro_value, piece_type
                    return True
                else:
                    self.indicator += 1
        return

    def board_behavior(self, arg_1, arg_2):
        self.arg_search1, self.arg_colors1 = arg_1, arg_2
        self.converter_to_list(messages.entry_1, messages.entry_2)
        self.colors(self.arg_colors1)
        self.search_of_pieces(self.actual_position, self.arg_search1, self.color)

    #  print("Funcioando")


board = Board()
# board.board_behavior(all_positions_of_pieces, 1)


class Pieces(Properies):
    def opposite_colors(self):
        if self.color == "black":
            self.pawn = 1
            self.opposite_color = "white"

        else:
            self.pawn = -1
            self.opposite_color = "black"
        self.piece_type_selected = board.pieces_type
        self.index_indicitor = board.indicator

    def dont_eat_your_team(self):
        if (
            board.search_of_pieces(
                self.pieces_position, all_positions_of_pieces, self.color
            )
            == True
        ):
            return False
        else:
            return True

    def attack_of_pieces(self):

        if (
            board.search_of_pieces(
                self.pieces_position, all_positions_of_pieces, self.opposite_color
            )
            == True
        ):
            all_positions_of_pieces[self.opposite_color][board.pieces_type][
                board.indicator
            ] = [
                None,
                None,
            ]
        return

    def vertical_movement(self, limit, i, reverse):
        while limit > 0:
            if reverse == True:

                if [
                    board.actual_position[0] - i,
                    board.actual_position[1],
                ] == self.pieces_position:
                    return True
            if [
                board.actual_position[0] + i,
                board.actual_position[1],
            ] == self.pieces_position:
                return True

            i += 1
            limit -= 1
        return False
    def horizonal_movement(self, limit, i, reverse):
        while limit > 0:
            if reverse == True:

                if (
                    letters_in_board[board.actual_position[1]] - i
                    == letters_in_board[self.pieces_position[1]]
                    and self.pieces_position[0] == board.actual_position[0]
                ):
                    return True

            if (
                letters_in_board[board.actual_position[1]] + i
                == letters_in_board[self.pieces_position[1]]
                and self.pieces_position[0] == board.actual_position[0]
            ):
                return True
            i += 1
            limit -= 1
        return False
    def lineal_movement(self, limit, i, reverse):
        # if (
        #      self.piece_types == "pawn"
        #      and board.search_of_pieces(
        #        self.pieces_position, all_positions_of_pieces, self.opposite_color
        #     )
        #   == None
        #  ):
        #    return
        while limit > 0:
            if reverse == True:

                if (
                    board.actual_position[0] - i == self.pieces_position[0]
                    and letters_in_board[board.actual_position[1]] - i
                    == letters_in_board[self.pieces_position[1]]
                ):
                    return True

                if (
                    board.actual_position[0] - i == self.pieces_position[0]
                    and letters_in_board[board.actual_position[1]] + i
                    == letters_in_board[self.pieces_position[1]]
                ):
                    return True

            if (
                board.actual_position[0] + i == self.pieces_position[0]
                and letters_in_board[board.actual_position[1]] + i
                == letters_in_board[self.pieces_position[1]]
            ):
                return True

            if (
                board.actual_position[0] + i == self.pieces_position[0]
                and letters_in_board[board.actual_position[1]] - i
                == letters_in_board[self.pieces_position[1]]
            ):
                return True
            i += 1
            limit -= 1
        return False
    def horse_movement(self):
        self.position_on_x = board.actual_position[0] - self.pieces_position[0]
        if self.position_on_x < 0:
            self.position_on_x *= -1
        self.position_on_y = (
            letters_in_board[board.actual_position[1]]
            - letters_in_board[self.pieces_position[1]]
        )
        if self.position_on_y < 0:
            self.position_on_y *= -1
        if self.position_on_x == 1 and self.position_on_y == 2:
            return True
        elif self.position_on_x == 2 and self.position_on_y == 1:
            return True
        return False
    def dont_go_through_pieces(self):
        if self.piece_types != "horses":
            self.letter_in_board = list(letters_in_board)
            self.numbers_between_actual_and_next_on_x = []
            self.numbers_between_actual_and_next_on_y = []
            if board.actual_position[0] > self.pieces_position[0]:
                x = self.pieces_position[0]
                while x < board.actual_position[0]:
                    self.numbers_between_actual_and_next_on_x.append(x)
                    x += 1
            elif board.actual_position[0] < self.pieces_position[0]:
                x = board.actual_position[0] + 1
                while x < self.pieces_position[0]:
                    self.numbers_between_actual_and_next_on_x.append(x)
                    x += 1

            if (
                letters_in_board[board.actual_position[1]]
                > letters_in_board[self.pieces_position[1]]
            ):
                y = letters_in_board[self.pieces_position[1]]
                while y < letters_in_board[board.actual_position[1]]:
                    self.numbers_between_actual_and_next_on_y.append(
                        self.letter_in_board[y - 1]
                    )
                    y += 1
            elif (
                letters_in_board[board.actual_position[1]]
                < letters_in_board[self.pieces_position[1]]
            ):
                y = letters_in_board[board.actual_position[1]] + 1
                while y < letters_in_board[self.pieces_position[1]]:
                    self.numbers_between_actual_and_next_on_y.append(
                        self.letter_in_board[y - 1]
                    )
                    y += 1
            if len(self.numbers_between_actual_and_next_on_x) == 0:
                self.numbers_between_actual_and_next_on_x.append(
                    self.pieces_position[0]
                )
            elif len(self.numbers_between_actual_and_next_on_y) == 0:
                self.numbers_between_actual_and_next_on_y.append(
                    self.pieces_position[1]
                )

            for color in all_positions_of_pieces:
                for x in self.numbers_between_actual_and_next_on_x:
                    for y in self.numbers_between_actual_and_next_on_y:
                        if (
                            board.search_of_pieces(
                                [x, y], all_positions_of_pieces, color
                            )
                            == True and [x,y] != self.pieces_position
                        ):
                            return False
            return True

    def pieces_behavior(self):
        self.opposite_colors()
        self.valid_movements = {
            "pawns": [
                self.vertical_movement(1, self.pawn, False),
                self.lineal_movement(1, self.pawn, False),
            ],
            "dame": [
                self.vertical_movement(8, 1, True),
                self.horizonal_movement(8, 1, True),
                self.lineal_movement(8, 1, True),
            ],
            "king": [
                self.vertical_movement(1, 1, True),
                self.horizonal_movement(1, 1, True),
                self.lineal_movement(1, 1, True),
            ],
            "horses": [self.horse_movement()],
            "towers": [
                self.horizonal_movement(8, 1, True),
                self.vertical_movement(8, 1, True),
            ],
            "bishops": [self.lineal_movement(8, 1, True)],
        }
        if self.piece_types == self.piece_type_selected:
            # print("Hay algo malo")
            #  print(self.valid_movements["pawns"][0], board.indicator,self.color)
            print(self.dont_eat_your_team())
            print(self.dont_go_through_pieces())
            for check in self.valid_movements[self.piece_types]:
                print(self.valid_movements[self.piece_types])
                if (
                    check == True
                    and self.dont_eat_your_team() != False
                    and self.dont_go_through_pieces() == True
                ):
                    #   print(self.piece_types)
                    if self.piece_types == "pawns":
                       
                        #    print(board.indicator,self.color)
                        if self.valid_movements[self.piece_types][1] == True:
                            self.attack_of_pieces()
                            print("Done!")
                        all_positions_of_pieces[self.color][self.piece_types][
                            self.index_indicitor
                        ] = self.pieces_position
                    elif self.piece_types != "pawns":
                        all_positions_of_pieces[self.color][self.piece_types][
                            self.index_indicitor
                        ] = self.pieces_position
                        self.attack_of_pieces()
                    return True
        return
