import chess_board
class Pawn(chess_board.Properies):
    @property
    def movements_pawn(self):
        self.walk_front(1)

    def attack_pawn(self, eaten, attaker):
        self.eat_in_chess(eaten, attaker)


class Dame(chess_board.Properies):
    @property
    def movement_1(self):
        self.walk_front(messages.entry_2)

    def movement_2(self):
        self.walk_back(messages.entry_2)

    def movement_3(self):
        self.walk_left(messages.entry_2)

    def movement_4(self):
        self.walk_right(messages.entry_2)

    def movement_5(self):
        self.walk_right(messages.entry_2)
        self.walk_front(messages.entry_2)

    def movement_6(self):
        self.walk_left(messages.entry_2)
        self.walk_front(messages.entry_2)

    def attack_dame(self, eaten, attaker):
        self.eat_in_chess(eaten, attaker)


class Bishop(chess_board.Properies):
    @property
    def movement_1(self):
        self.walk_right(messages.entry_2)
        self.walk_front(messages.entry_2)

    def movement_2(self):
        self.walk_left(messages.entry_2)
        self.walk_front(messages.entry_2)

    def attack_bishop(self, eaten, attaker):
        self.eat_in_chess(eaten, attaker)


class Tower(chess_board.Properies):
    @property
    def movement_1(self):
        self.walk_front(messages.entry_2)

    def movement_2(self):
        self.walk_back(messages.entry_2)

    def movement_3(self):
        self.walk_left(messages.entry_2)

    def movement_4(self):
        self.walk_right(messages.entry_2)

    def attack_tower(self, eaten, attaker):
        self.eat_in_chess(eaten, attaker)


class King(chess_board.Properies):
    @property
    def movement_1(self):
        self.walk_front(1)

    def movement_2(self):
        self.walk_back(1)

    def movement_3(self):
        self.walk_left(1)

    def movement_4(self):
        self.walk_right(1)

    def movement_5(self):
        self.walk_right(1)
        self.walk_front(1)

    def movement_6(self):
        self.walk_left(1)
        self.walk_front(1)

    def attack_king(self, eaten, attaker):
        self.eat_in_chess(eaten, attaker)

