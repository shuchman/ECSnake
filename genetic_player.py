import numpy as np
from game import MOVES, FOOD, EMPTY
import math

window_size = 7
hidden_size = 15
board_size = 10


class GeneticPlayer:
    def __init__(self, brain):
        self.window_size = window_size
        self.hidden_size = hidden_size
        self.board_size = board_size
        self.brain = brain

    def next_move(self, board, snake):
        input_vector = self.process_board(board, snake[-1][0], snake[-1][1], snake)
        hidden_layer1 = self.brain[0]
        hidden_layer2 = self.brain[1]
        output_layer = self.brain[2]

        # forward propagation, dot product
        hidden_result1 = np.array([
                                      math.tanh(np.dot(input_vector, hidden_layer1[i]))
                                      for i in range(hidden_layer1.shape[0])] + [1])  # [1] for bias

        hidden_result2 = np.array([
                                      math.tanh(np.dot(hidden_result1, hidden_layer2[i]))
                                      for i in range(hidden_layer2.shape[0])] + [1])  # [1] for bias

        output_result = np.array([
            math.tanh(np.dot(hidden_result2, output_layer[i]))
            for i in range(output_layer.shape[0])])

        max_index = np.argmax(output_result)
        return MOVES[max_index]

    def process_board(self, board, x, y, snake):
        input_vector = [
            [0 for _ in range(self.window_size)]
            for _ in range(self.window_size)]

        for i in range(self.window_size):
            for j in range(self.window_size):
                ii = x + i - self.window_size // 2
                jj = y + j - self.window_size // 2

                if ii < 0 or jj < 0 or ii >= self.board_size or jj >= self.board_size:
                    input_vector[i][i] = -1
                elif (ii, jj) in snake:
                    input_vector[i][j] = -1
                elif board[ii][jj] == FOOD:
                    input_vector[i][j] = 1
                elif board[ii][jj] == EMPTY:
                    input_vector[i][j] = 0
                else:
                    input_vector[i][j] = -1

        input_vector = list(np.array(input_vector).flatten()) + [1]
        return np.array(input_vector)
