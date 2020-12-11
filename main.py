from chess_board import all_positions_of_pieces
from chess_board import letters_in_board
from chess_board import messages
from chess_board import board
from chess_board import Pieces
#def main():
 # print("Hola")


turn = 0
while True:
 turn += 1
 messages.menu()
 board.board_behavior(all_positions_of_pieces,turn)
 #pawn = Pieces(board.next_position, board.color, "pawns")
 #horse = Pieces(board.next_position, board.color, "horses")
 #bishop = Pieces(board.next_position, board.color, "bishops")
 #dame = Pieces(board.next_position, board.color, "dame")
 king = Pieces(board.next_position, board.color, "king")
 #tower = Pieces(board.next_position, board.color, "towers")



 #pawn.pieces_behavior()
 #bishop.pieces_behavior()
 #horse.pieces_behavior()
 #dame.pieces_behavior()
 king.pieces_behavior()
# tower.pieces_behavior()


 