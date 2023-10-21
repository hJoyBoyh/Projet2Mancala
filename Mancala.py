import random

class Mancala:
    def __init__(self):
        self.grille = {
            "A": 4,
            "B": 4,
            "C": 4,
            "D": 4,
            "E": 4,
            "F": 4,
            "2": 0,
            "L": 4,
            "K": 4,
            "J": 4,
            "I": 4,
            "H": 4,
            "G": 4,
            "1": 0,
        }
        self.joueurTour = random.choice([True, False])

    def joueurDeplacement(self, id):
        if not self.joueurTour or id in "GHIJKL21" or self.grille[id] == 0:
            return False

        bumps = self.grille[id]
        self.grille[id] = 0
        current_key = id
        replay = False

        while bumps > 0:
            current_key = self.get_next_key(current_key)
            if current_key == "2":
                self.grille["2"] += 1
                bumps -= 1
                if bumps == 0:
                    replay = True
            else:
                self.grille[current_key] += 1
                bumps -= 1
                if bumps == 0 and self.grille[current_key] == 1:
                    opposite_key = self.get_opposite_key(current_key)
                    if opposite_key and self.grille[opposite_key] > 0:
                        self.grille["2"] += 1 + self.grille[opposite_key]
                        self.grille[opposite_key] = 0
                        self.grille[current_key] = 0
        
        self.joueurTour = replay

        return True

    def ordiDeplacement(self, agent="random"):
        self.getValidMoves(self.grille, True)
        if agent == "random":
            return self.randomAgent()
        elif agent == "minmax":
            return self.minMaxAgent()
        elif agent == "max":
            return self.maxAgent()
        else:
            return False

    def randomAgent(self):
        if self.joueurTour:
            return False

        blacklist = "ABCDEF21"

        valid_moves = [key for key, value in self.grille.items() if key not in blacklist and value > 0] # list comprehension

        if not valid_moves:
            return "end game"

        move = random.choice(valid_moves)
        self.makeMove(self.grille, move)
        print(f"Random Agent: Chose Move = {move}")
        return True

    def minMaxAgent(self):
        if self.joueurTour:
            return False

        _, move = self.minMax(self.grille.copy(), True, depth=3)
        if move:
            self.makeMove(self.grille, move)
            print(f"MinMax Agent: Chose Move = {move}")
            return True
        return False

    def maxAgent(self):
        if self.joueurTour:
            return False

        grilleCopy = self.grille.copy()
        _, move = self.maximize(grilleCopy, True, 6)
        if move:
            self.makeMove(self.grille, move)
            print(f"Max Agent: Chose Move = {move}")
            return True
        return "end game"

    def minMax(self, board, maximizing, depth):
        if depth == 0 or self.isTerminal(board, maximizing):
            score = self.evaluate(board)
            return score, None

        if maximizing:
            max_eval = float('-inf')
            best_move = None
            for move in self.getValidMoves(board, maximizing):
                new_board = self.makeMove(board.copy(), move)
                evaluation, _ = self.minMax(new_board, maximizing, depth - 1)
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
            #print(f"MinMax Depth {depth}: Best Move = {best_move}, Max Eval = {max_eval}")
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in self.getValidMoves(board, maximizing):
                new_board = self.makeMove(board.copy(), move)
                evaluation, _ = self.minMax(new_board, maximizing, depth - 1)
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
            #print(f"MinMax Depth {depth}: Best Move = {best_move}, Min Eval = {min_eval}")
            return min_eval, best_move

    def maximize(self, board, maximizing, depth):
        if depth == 0 or self.isTerminal(board, maximizing):
            score = self.evaluate(board)
            return score, None
        
        max_eval = float('-inf')
        best_move = None
        valid_moves = self.getValidMoves(board, maximizing)
        for move in valid_moves:
            new_board = self.makeMove(board.copy(), move)
            evaluation, _ = self.minMax(new_board, False, depth - 1)
            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move
        print(f"Maximize Depth {depth}: Best Move = {best_move}, Max Eval = {max_eval}")
        return max_eval, best_move

    def evaluate(self, board):
        if board is None:
            return 0
        player_a_score = sum(board[key] for key in "ABCDEF2")
        player_b_score = sum(board[key] for key in "GHIJKL1")

        return player_a_score - player_b_score

    def isTerminal(self, board, maximising):
        return not self.getValidMoves(board, maximising)
    
    def terminateGame(self):
        player_a_score = sum(self.grille[key] for key in "ABCDEF")
        player_b_score = sum(self.grille[key] for key in "GHIJKL")

        if player_a_score == 0 or player_b_score == 0:
            player = sum(self.grille[key] for key in "ABCDEF2")
            AI = sum(self.grille[key] for key in "GHIJKL1")

            for key, value in self.grille.items():
                self.grille[key] = 0
                if key == "2":
                    self.grille[key] = player
                elif key == "1":
                    self.grille[key] = AI
            return True
        else:
            return False

    def getValidMoves(self, board, maximizing):
        valid_moves = []
        if board:
            valid_moves = [key for key, value in board.items() if (maximizing and key not in "ABCDEF21" and value > 0) or (not maximizing and key not in "GHIJKL21" and value > 0)]
            if valid_moves == []:
                self.terminateGame()
        return valid_moves

    def makeMove(self, board, move):
        bumps = self.grille[move]
        board[move] = 0
        current_key = move
        replay = False

        while bumps > 0:
            current_key = self.get_next_key(current_key)
            if current_key == "1":
                board["1"] += 1
                bumps -= 1
                if bumps == 0:
                    replay = True
            else:
                board[current_key] += 1
                bumps -= 1
                if bumps == 0 and board[current_key] == 1:
                    opposite_key = self.get_opposite_key(current_key)
                    if opposite_key and board[opposite_key] > 0:
                        board["1"] += 1 + board[opposite_key]
                        board[opposite_key] = 0
                        board[current_key] = 0

        self.joueurTour = not replay
        
        return board

    def get_next_key(self, key):
        keys = list(self.grille.keys())
        index = keys.index(key)
        index = (index + 1) % len(keys)
        return keys[index]

    def get_opposite_key(self, key):
        opposite_keys = {
            "A": "G",
            "B": "H",
            "C": "I",
            "D": "J",
            "E": "K",
            "F": "L",
            "G": "A",
            "H": "B",
            "I": "C",
            "J": "D",
            "K": "E",
            "L": "F",
        }
        return opposite_keys.get(key, None)