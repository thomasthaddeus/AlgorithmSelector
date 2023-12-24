class Minimax:
    def __init__(self, depth, game):
        self.depth = depth
        self.game = game

    def minimax(self, depth, is_maximizing_player):
        """Perform the Minimax algorithm."""
        if depth == 0 or self.game.is_game_over():
            return self.game.evaluate()

        if is_maximizing_player:
            best_val = -float('inf')
            for move in self.game.get_possible_moves():
                self.game.make_move(move)
                value = self.minimax(depth - 1, False)
                best_val = max(best_val, value)
                self.game.undo_move(move)
            return best_val
        else:
            best_val = float('inf')
            for move in self.game.get_possible_moves():
                self.game.make_move(move)
                value = self.minimax(depth - 1, True)
                best_val = min(best_val, value)
                self.game.undo_move(move)
            return best_val

    def find_best_move(self):
        """Find the best move for the current player."""
        best_move = None
        best_val = -float('inf') if self.game.is_maximizing_players_turn() else float('inf')

        for move in self.game.get_possible_moves():
            self.game.make_move(move)
            move_val = self.minimax(self.depth - 1, not self.game.is_maximizing_players_turn())
            self.game.undo_move(move)

            if self.game.is_maximizing_players_turn() and move_val > best_val:
                best_move = move
                best_val = move_val
            elif not self.game.is_maximizing_players_turn() and move_val < best_val:
                best_move = move
                best_val = move_val

        return best_move

# Example usage
# This example assumes a 'Game' class with methods: get_possible_moves, make_move, undo_move, evaluate, is_game_over, and is_maximizing_players_turn
# game = Game()
# minimax = Minimax(depth=3, game=game)
# best_move = minimax.find_best_move()
# print("Best move:", best_move)
