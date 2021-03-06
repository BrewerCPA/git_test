import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = self.make_board() # List of length 9 for 3x3 board
        self.current_winner = None # keep track of winner!

    @staticmethod
    def make_board():
        return [" " for _ in range(9)]


    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod # won't relate to any specific board, so no self necessary
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def make_move(self, square, letter):
        # if valid move, make move and return True--> else return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter): 
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check board for winner
        # check row
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind+1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3]  for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        if square % 2 ==0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal1]):
                return True
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']
       
    def empty_squares(self):
        # check for empty squares
        return " " in self.board # returns boolean

    def num_empty_squares(self):
        return self.board.count(' ')  # len(self.ava

def play(game, x_player, o_player, print_game=True):
    # returns winner of game or None for tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # iterate while game still has empty squares
    while game.empty_squares():
        # get move from appropriate player
        if letter == '0':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # define move function
        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + '  wins!')
                return letter

            # alternate letters after made move
            letter = '0' if letter == 'X' else 'X'
        
        time.sleep(1)

    if print_game:
        print('Tie Game')


    

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('0')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)