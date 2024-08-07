import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_box = False
        val = None
        while not valid_box:
            box = input(self.letter + '\'s turn. Input position on board (1-9): ')
            try:
                val = int(box) - 1  # Adjust for 0-based index
                if val not in game.available_moves():
                    raise ValueError
                valid_box = True
            except ValueError:
                print('Invalid move. Please try again.')
        return val
    
class Computer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            box = random.choice(game.available_moves())
        else:
            box = self.minimax(game, self.letter)['position']
        return box
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.number_empty_box() + 1)
                    if other_player == max_player
                    else -1 * (state.number_empty_box() + 1)}
        elif not state.empty_box():
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
