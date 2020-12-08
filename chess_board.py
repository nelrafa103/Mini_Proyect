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
        "horses": [[1, "B"], [2, "G"]],
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
messages.menu()


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
        ##print(self.actual_position)
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


board = Board()
board.board_behavior(all_positions_of_pieces, 2)


class Pieces(Properies):
    def opposite_colors(self):
     if self.color == "black":
        self.pawn = 1
        self.opposite_color = "white"
      
     else:
        self.pawn = -1
        self.opposite_color = "black"
     

    def attack_of_pieces(self):
        def dont_eat_you_team():
            while True:
             
             return

        def attack_pieces(self):
          
            if (
                board.search_of_chips(
                    self.position, all_positions_of_pieces, self.opposite_color
                )
                == True
            ):
                all_positions_of_pieces[self.opposite_color][board.chip_type][
                    board.indicator
                ] = [
                    None,
                    None,
                ]
            return

    def movement_of_pieces(self):
        def vertical_movement(limit,i,reverse):
          while limit > 0:   
            if reverse == True:
             if [board.actual_position[0] - i,board.actual_position[1]] == self.pieces_position:
                return True
            if [board.actual_position[0] + i,board.actual_position[1]] == self.pieces_position:
                return True
            i += 1
            limit -= 1
        def horizonal_movement(limit,i,reverse):
          while limit > 0:   
            if reverse == True:
             if letters_in_board [board.actual_position[1]] - i == letters_in_board[self.pieces_position[1]] and self.pieces_position[0] == board.actual_position[0]:
                return True
            if letters_in_board[board.actual_position[1]] + i == letters_in_board[self.pieces_position[1]] and self.pieces_position[0] == board.actual_position[0]:
                return True
            i += 1
            limit -= 1
    
        def lineal_movement(limit,i,reverse):
          while limit > 0:   
        #    if reverse == True:
          #      if board.actual_position[0] - i == self.pieces_position[0] and letters_in_board [board.actual_position[1]] - i == self.pieces_position[1]:
           #      return True
          #      if board.actual_position[0] - i == self.pieces_position[0] and letters_in_board [board.actual_position[1]] + i == self.pieces_position[1]:
           #      return True
        #    else:
             if board.actual_position[0] + i == self.pieces_position[0] and letters_in_board [board.actual_position[1]] + i == self.pieces_position[1]:
              return True             
              print( board.actual_position[0] + i == self.pieces_position[0],letters_in_board [board.actual_position[1]] + i )
             if  board.actual_position[0] + i == self.pieces_position[0] and letters_in_board [board.actual_position[1]] - i == self.pieces_position[1]:
              return True
              print( board.actual_position[0] + i == self.pieces_position[0],letters_in_board [board.actual_position[1]] - i)
             i += 1
             limit -= 1;
        valid_movements = {
            "pawns": [vertical_movement(1,self.pawn,False),lineal_movement(1,self.pawn,False)],
            "dame": [vertical_movement(8,1,True),horizonal_movement(8,1,True)],
            "king": [vertical_movement(1, 1,True),horizonal_movement(1,1,True)],
            "horses": [False],
           "towers": [False],
           "bishops": [False],
        }
        print(valid_movements[self.piece_types])
       # return6.000000        Monto:  56.000000
#Ciudad con menor venta: Id:     1.00000


pawn = Pieces(board.next_position, board.color, "pawns")
horse = Pieces(board.next_position, board.color, "horses")
bishop = Pieces(board.next_position, board.color, "bishops")
dame = Pieces(board.next_position, board.color, "dame")
king = Pieces(board.next_position, board.color, "king")
tower = Pieces(board.next_position, board.color, "towers")
pawn.opposite_colors()
pawn.movement_of_pieces()

#horse.movement_of_pieces()
#bishop.movement_of_pieces()
dame.opposite_colors()
dame.movement_of_pieces()
king.opposite_colors()
king.movement_of_pieces()
#tower.movement_of_pieces()
