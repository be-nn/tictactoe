import math
import time
from allplayers import Human, Computer

class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_numbers():
        # 1 | 2 | 3
        # 4 | 5 | 6
        # 7 | 8 | 9
        number_board = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, box, letter):
        if self.board[box] == ' ':
            self.board[box] = letter
            if self.winner(box, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, box, letter):
        # row
        row_ind = math.floor(box / 3)
        row = self.board[row_ind*3: (row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        # column
        col_ind = box % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        # diagonal
        if box % 2 == 0:
            diagonal_right = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal_right]):
                return True
            diagonal_left = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal_left]):
                return True
        return False

    def empty_box(self):
        return ' ' in self.board

    def number_empty_box(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

def play(game, playerx, playero, print_game=True):
    if print_game:
        game.print_board_numbers()

    letter = 'X'  # X always goes first
    while game.empty_box():
        if letter == 'O':
            box = playero.get_move(game)
        else:
            box = playerx.get_move(game)
        if game.make_move(box, letter):
            if print_game:
                print(letter + f' makes a move to box {box}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    playerx = Computer('X')
    playero = Human('O')
    t = TicTacToe()
    play(t, playerx, playero, print_game=True)
