def show(chessboard):
    """Shows the chessboard in the console.
    DOES NOT WORK UNTIL ALL CLASSES: Pawn, Knight, Queen, King, Rook, Bishop ARE CREATED!!!
    """
    WHITE = {
        Pawn: chr(9817),
        Knight: chr(9816),
        Queen: chr(9813),
        King: chr(9812),
        Rook: chr(9814),
        Bishop: chr(9815),
    }
    BLACK = {
        Pawn: chr(9823),
        Knight: chr(9818),
        Queen: chr(9819),
        King: chr(9812),
        Rook: chr(9820),
        Bishop: chr(9821),
    }
    for y in range(7, -1, -1):
        print(y, end='\t')
        for x in range(8):
            if chessboard.board[x][y] is not None:
                if chessboard.board[x][y].color == 'white':
                    print(WHITE[type(chessboard.board[x][y])], end='\t')
                else:
                    print(BLACK[type(chessboard.board[x][y])], end='\t')
            else:
                print('\t', end='')
        print('\n')
    print('\t', end='')
    for x in range(8):
        print(x, end='\t')
    print()


WHITE = 'white'
BLACK = 'black'


class Chessboard:
    def __init__(self):
        self.color = WHITE
        self.board = [[None] * 8 for _ in range(8)]

    def list_allowed_moves(self, x, y):
        figure = self.board[x][y]
        if figure is None:
            return None

        if figure.color != self.color:
            return None

        allowed_moves = figure.list_allowed_moves(self)
        return allowed_moves


    def is_still_on_board(self, x, y):
        if x < 0 or y < 0:
            return False
        if x >= len(self.board):
            return False
        if y >= len(self.board[0]):
            return False
        return True

    def setup(self):
        def set_player_figures(color, pawns_row, figures_row):
            higher_figures = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
            for i, figure_class in enumerate(higher_figures):
                figure = figure_class(color, i, figures_row)
                self.board[i][figures_row] = figure

            for i in range(8):
                pawn = Pawn(color, i, pawns_row)
                self.board[i][pawns_row] = pawn

        set_player_figures(WHITE, pawns_row=1, figures_row=0)
        set_player_figures(BLACK, pawns_row=6, figures_row=7)

    def move(self, from_x, from_y, to_x, to_y):
        allowed_moves = self.list_allowed_moves(from_x, from_y)
        if allowed_moves is None:
            allowed_moves = []

        if (to_x, to_y) not in allowed_moves:
            raise ValueError

        figure = self.board[from_x][from_y]
        self.board[to_x][to_y] = figure
        self.board[from_x][from_y] = None
        figure.move(to_x, to_y)

        self._switch_player()

    def _switch_player(self):
        if self.color == BLACK:
            self.color = WHITE
        else:  # self.color == WHITE
            self.color = BLACK


class Figure:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def _get_diagonal_moves(self):
        return [
            (1, 1),
            (1, -1),
            (-1, -1),
            (-1, 1),
        ]

    def _get_vertical_moves(self):
        return [
            (0, 1),
            (0, -1),
        ]

    def _get_horizontal_moves(self):
        return [
            (1, 0),
            (-1, 0),
        ]

    def _get_horizontal_and_vertical_moves(self):
        return self._get_vertical_moves() + self._get_horizontal_moves()

    def _list_allowed_moves(self, possible_directions, chessboard, max_move_length=None):
        possible_moves = []
        if not max_move_length:
            max_move_length = len(chessboard.board) - 1

        for direction in possible_directions:
            for move_length in range(1, max_move_length + 1):
                new_location_x = self.x + move_length * direction[0]
                new_location_y = self.y + move_length * direction[1]

                if not chessboard.is_still_on_board(new_location_x, new_location_y):
                    break

                figure = chessboard.board[new_location_x][new_location_y]
                if figure is None:
                    possible_moves.append((new_location_x, new_location_y))
                    continue

                if figure.color != self.color:
                    possible_moves.append((new_location_x, new_location_y))
                break
        return possible_moves


class Pawn(Figure):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.already_moved = False

    def list_allowed_moves(self, chessboard):
        move_index = 0 if self.color == WHITE else 1
        possible_directions = [self._get_vertical_moves()[move_index]]

        max_move_length = 1 if self.already_moved else 2
        possible_moves = self._list_allowed_moves(possible_directions, chessboard,
                                                  max_move_length=max_move_length)

        return possible_moves

    def move(self, x, y):
        super().move(x, y)
        self.already_moved = True


class Rook(Figure):
    def list_allowed_moves(self, chessboard):
        possible_directions = self._get_horizontal_and_vertical_moves()

        possible_moves = self._list_allowed_moves(possible_directions, chessboard)
        return possible_moves


class King(Figure):
    def list_allowed_moves(self, chessboard):
        possible_directions = self._get_horizontal_and_vertical_moves() + self._get_diagonal_moves()

        possible_moves = self._list_allowed_moves(possible_directions, chessboard, max_move_length=1)
        return possible_moves


class Bishop(Figure):
    def list_allowed_moves(self, chessboard):
        possible_directions = self._get_diagonal_moves()

        possible_moves = self._list_allowed_moves(possible_directions, chessboard)
        return possible_moves


class Queen(Figure):
    def list_allowed_moves(self, chessboard):
        possible_directions = self._get_horizontal_and_vertical_moves() + self._get_diagonal_moves()

        possible_moves = self._list_allowed_moves(possible_directions, chessboard)
        return possible_moves


class Knight(Figure):
    def list_allowed_moves(self, chessboard):
        possible_directions = [
            (1, 2), (2, 1), (2, -1), (1, -2),
            (-1, -2), (-2, -1), (-2, 1), (-1, 2),
        ]

        possible_moves = self._list_allowed_moves(possible_directions, chessboard, max_move_length=1)
        return possible_moves