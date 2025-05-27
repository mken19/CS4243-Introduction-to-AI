from typing import Tuple, List, Literal
from copy import deepcopy
class State:
    piece_values = {"King": 100, "Knight": 3, "Bishop": 3, "Rook": 5, "Squire": 3, "Combatant": 2}
    def __init__(self, gameboard, white_score=None, black_score=None):
        self.gameboard = gameboard
        if white_score is None or black_score is None:
            self.white_score = self.get_score("white")
            self.black_score = self.get_score("black")
        else:
            self.white_score = white_score
            self.black_score = black_score
        self.is_terminal = False
    def get_score(self, color):
        score = 0
        for pos, piece in self.gameboard.get_pieces(color).items():
            score += State.piece_values[piece]
        return score
    def make_move(self, color, move):
        new_state = deepcopy(self)
        is_captured, piece = new_state.gameboard.shift(color, move[0], move[1])
        if is_captured:
            if color == "white":
                new_state.black_score -= State.piece_values[piece]
            else:
                new_state.white_score -= State.piece_values[piece]
        if piece == "King" or new_state.king_moves(color) == 0:
            new_state.is_terminal = True
        return new_state
    def get_legal_moves(self, color):
        return get_legal_moves(self.gameboard.get_list(), color)
    def evaluate(self):
        return self.white_score - self.black_score
    def king_moves(self, color):
        for pos, piece in self.gameboard.get_pieces(color).items():
            if piece == 'King':
                possible_moves = []
                x, y = pos
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        new_pos = (x + dx, y + dy)
                        if self.gameboard.is_valid_move(color, new_pos):
                            possible_moves.append((pos, new_pos))
                return len(possible_moves)
class Board:
    def __init__(self, board):
        self.gameboard = {"black": {}, "white": {}}
        for piece, color, pos in board:
            self.gameboard[color][pos] = piece
    def is_valid_move(self, color,pos):
        return 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7 and pos not in self.gameboard[color]
    def is_valid_capture(self, color, pos):
        opp_color = "white" if color == "black" else "black"
        return 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7 and pos in self.gameboard[opp_color]
    def get_pieces(self, color):
        return self.gameboard[color]
    def get_list(self):
        board_list = []
        for pos, piece in self.gameboard["white"].items():
            board_list.append((piece, "white", pos))
        for pos, piece in self.gameboard["black"].items():
            board_list.append((piece, "black", pos))
        return board_list
    def shift(self, color, pos1, pos2):
        piece = self.gameboard[color].pop(pos1)
        self.gameboard[color][pos2] = piece
        opp_color = "white" if color == "black" else "black"
        if (pos2 in self.gameboard[opp_color]):
            captured_piece = self.gameboard[opp_color].pop(pos2)
            return True, captured_piece
        return False, None
def get_legal_moves(board, color):
    gameboard = Board(board)
    def get_king_moves(pos):
        normal_moves = []
        capture_moves = []
        x, y = pos
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                new_pos = (x + dx, y + dy)
                if gameboard.is_valid_capture(color, new_pos):
                    capture_moves.append((pos, new_pos))
                else:
                    if gameboard.is_valid_move(color, new_pos):
                        normal_moves.append((pos, new_pos))
        return normal_moves, capture_moves
    def get_rook_moves(pos):
        normal_moves = []
        capture_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            x, y = pos
            while True:
                new_pos = (x + dx, y + dy)
                if gameboard.is_valid_capture(color, new_pos):
                    capture_moves.append((pos, new_pos))
                    break
                else:
                    if gameboard.is_valid_move(color, new_pos):
                        normal_moves.append((pos, new_pos))
                    else:
                        break
                x, y = new_pos
        return normal_moves, capture_moves
    def get_bishop_moves(pos):
        normal_moves = []
        capture_moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in directions:
            x, y = pos
            while True:
                new_pos = (x + dx, y + dy)
                if gameboard.is_valid_capture(color, new_pos):
                    capture_moves.append((pos, new_pos))
                    break
                else:
                    if gameboard.is_valid_move(color, new_pos):
                        normal_moves.append((pos, new_pos))
                    else:
                        break
                x, y = new_pos
        return normal_moves, capture_moves
    def get_knight_moves(pos):
        normal_moves = []
        capture_moves = []
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for dx, dy in directions:
            x, y = pos
            new_pos = (x + dx, y + dy)
            if gameboard.is_valid_capture(color, new_pos):
                capture_moves.append((pos, new_pos))
            else:
                if gameboard.is_valid_move(color, new_pos):
                    normal_moves.append((pos, new_pos))
        return normal_moves, capture_moves
    def get_squire_moves(pos):
        normal_moves = []
        capture_moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (2, 0), (-2, 0), (0, 2), (0, -2)]
        for dx, dy in directions:
            x, y = pos
            new_pos = (x + dx, y + dy)
            if gameboard.is_valid_capture(color, new_pos):
                capture_moves.append((pos, new_pos))
            else:
                if gameboard.is_valid_move(color, new_pos):
                    normal_moves.append((pos, new_pos))
        return normal_moves, capture_moves
    def get_combatant_moves(pos):
        normal_moves = []
        capture_moves = []
        move_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        capture_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in capture_directions:
            x, y = pos
            new_pos = (x + dx, y + dy)
            if gameboard.is_valid_capture(color, new_pos):
                capture_moves.append((pos, new_pos))
        for dx, dy in move_directions:
            x, y = pos
            new_pos = (x + dx, y + dy)
            if gameboard.is_valid_move(color, new_pos) and not gameboard.is_valid_capture(color, new_pos):
                normal_moves.append((pos, new_pos))
        return normal_moves, capture_moves
    move_ordering = {
        'King': get_king_moves,
        'Rook': get_rook_moves,
        'Bishop': get_bishop_moves,
        'Knight': get_knight_moves,
        'Squire': get_squire_moves,
        'Combatant': get_combatant_moves,
    }
    ordered_moves = []
    legal_moves = []
    for pos, piece in gameboard.get_pieces(color).items():
        moves_func = move_ordering[piece]
        normal_moves, capture_moves = moves_func(pos)
        ordered_moves.extend(capture_moves)
        legal_moves.extend(normal_moves)
    ordered_moves.extend(legal_moves)
    return ordered_moves
def studentAgent(board):
    gameboard = Board(board)
    initial_state = State(gameboard)
    legal_moves = get_legal_moves(board, "white")
    best_move = None
    best_value = float('-inf')
    alpha = float('-inf')
    beta = float('inf')
    depth = 5
    for move in legal_moves:
        new_state = initial_state.make_move("white", move)
        value = ab(new_state, depth - 1, alpha, beta, "black")
        if value > best_value:
            best_value = value
            best_move = move
        alpha = max(alpha, value)
    return best_move
def ab(state, depth, alpha, beta, player):
    if state.is_terminal:
        if player == "white": # white is terminated
            return float('-inf')
        else:
            return float('inf')
    if depth == 0:
        return state.evaluate()
    if player == "white":
        value = float('-inf')
        legal_moves = get_legal_moves(state.gameboard.get_list(), "white") # get legal moves
        for move in legal_moves:
            new_state = state.make_move("white", move)
            value = max(value, ab(new_state, depth - 1, alpha, beta, "black"))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        legal_moves = get_legal_moves(state.gameboard.get_list(), "black")
        for move in legal_moves:
            new_state = state.make_move("black", move)
            value = min(value, ab(new_state, depth - 1, alpha, beta, "white"))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value