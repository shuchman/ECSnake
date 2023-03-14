#Didya code:

import numpy as np
import tkinter as tk
import time as time
import random as rand

# global
board_size = 10
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

MOVES = [UP, DOWN, LEFT, RIGHT]

EMPTY = 0
FOOD = 99


class Game:
    def __init__(self, player, gui=None, display=False):
        self.size = board_size
        self.player = player
        self.display = display
        self.max_turns = 300
        self.should_terminate = False

        self.num_food = 4
        self.turn = 0
        self.snake_size = 3

        self.snake = [                                     # generate init snake
            (self.size // 2, self.size // 2 + i)
            for i in range(self.snake_size)]

        self.food = [                                      # place init food
            (self.size // 4, self.size // 4),
            (3 * self.size // 4, self.size // 4),
            (self.size // 4, 3 * self.size // 4),
            (3 * self.size // 4, 3 * self.size // 4),
        ]

        self.board = np.zeros([self.size, self.size])       # init board

        if gui is not None:
            self.gui = Gui(self,10)

        for snake_unit in self.snake:                       # mark snake on board
            self.board[snake_unit[0]][snake_unit[1]] = 1    # mark food on board

        for food_unit in self.food:
            self.board[food_unit[0]][food_unit[1]] = FOOD

        self.food_index = 0
        self.food_xy = [
            (2, 4),
            (8, 2),
            (4, 4),
            (9, 5),
            (9, 2),
            (7, 5),
            (5, 5),
            (6, 2),
            (7, 8),
            (6, 5),
            (3, 9),
            (5, 6),
            (9, 3),
            (4, 8),
            (4, 4),
            (5, 5),
            (5, 7),
            (9, 3),
            (3, 2),
            (5, 1),
            (7, 1),
            (8, 6),
            (4, 1),
            (7, 3),
            (4, 5),
            (1, 9),
            (6, 3),
            (4, 7),
            (6, 5),
            (1, 0),
            (2, 8),
            (5, 1),
            (1, 7),
            (6, 0),
            (9, 0),
            (7, 9),
            (7, 6),
            (9, 8),
            (5, 5),
            (0, 8),
            (2, 0),
            (3, 1),
            (7, 4),
            (2, 0),
            (2, 8),
            (2, 3),
            (9, 1),
            (7, 4),
            (2, 9),
            (1, 4),
            (7, 0),
            (1, 8),
            (6, 9),
            (4, 9),
            (2, 3),
            (0, 7),
            (1, 3),
            (2, 2),
            (0, 6),
            (9, 9),
            (2, 8),
            (7, 9),
            (7, 3),
            (0, 6),
            (1, 4),
            (6, 7),
            (1, 5),
            (8, 9),
            (2, 9),
            (1, 8),
            (2, 8),
            (2, 3),
            (9, 1),
            (7, 4),
            (2, 9),
            (1, 4),
            (7, 0),
            (1, 8),
            (6, 9),
            (4, 9),
            (2, 3),
            (0, 7),
            (1, 3),
            (2, 2),
            (0, 6),
            (9, 9),
            (2, 8),
            (7, 9),
            (7, 3),
            (0, 6),
            (1, 4),
            (6, 7),
            (1, 5),
            (8, 9),
            (2, 9),
            (1, 8),
            (3, 7),
            (2, 2),
            (7, 2),
            (2, 6),
            (3, 1),
            (2, 9),
            (0, 3),
            (2, 0),
            (5, 7),
            (7, 4),
            (5, 0),
            (4, 3),
            (1, 2),
            (5, 4),
            (3, 4),
            (7, 3),
            (3, 3),
            (4, 7),
            (9, 3),
            (4, 1),
            (0, 7),
            (3, 1),
            (7, 6),
            (6, 1),
            (5, 1),
            (1, 7),
            (2, 5),
            (4, 2),
            (9, 3),
            (4, 7),
            (4, 5),
            (7, 9),
            (7, 3),
            (0, 3),
            (1, 8),
            (2, 9),
            (7, 8),
            (7, 9),
            (3, 8),
            (6, 3),
            (3, 5),
            (4, 1),
            (1, 3),
            (1, 5),
            (4, 1),
            (5, 7),
            (3, 4),
            (3, 5),
            (9, 4),
            (7, 5),
            (3, 3),
            (5, 3),
            (1, 0),
            (5, 3),
            (4, 1),
            (8, 1),
            (5, 5),
            (4, 4),
            (7, 6),
            (5, 4),
            (3, 9),
            (7, 2),
            (0, 4),
            (7, 1),
            (7, 6),
            (5, 6),
            (4, 7),
            (8, 0),
            (0, 9),
            (5, 7),
            (3, 7),
            (1, 7),
            (6, 0),
            (6, 7),
            (3, 1),
            (1, 9),
            (0, 8),
            (1, 3),
            (8, 2),
            (8, 8),
            (0, 3),
            (3, 9),
            (9, 6),
            (5, 1),
            (2, 8),
            (9, 9),
            (5, 0),
            (0, 0),
            (2, 2),
            (8, 4),
            (1, 3),
            (7, 9),
            (9, 4),
            (3, 6),
            (2, 4),
            (7, 0),
            (0, 0),
            (6, 8),
            (7, 7),
            (8, 9),
            (5, 4),
            (7, 1),
            (4, 5),
            (2, 2),
            (0, 3),
            (7, 6),
            (9, 2),
            (9, 6),
            (9, 6),
            (1, 2),
            (5, 1),
            (2, 3),
            (2, 1),
            (8, 0),
            (0, 9),
            (5, 7),
            (7, 6),
            (6, 8),
            (3, 3),
            (0, 8),
            (3, 9),
            (2, 6),
            (7, 6),
            (2, 6),
            (0, 5),
            (5, 4),
            (2, 4),
            (5, 2),
            (8, 1),
            (7, 7),
            (7, 2),
            (8, 5),
            (9, 0),
        ]

    def move(self):
        # move the head
        snake = self.snake
        move = self.player.next_move(self.board, snake)
        new_square = (snake[-1][0] + move[0], snake[-1][1] + move[1])
        if new_square in snake:
            self.should_terminate = True
        snake.append(new_square)

        # update tail
        head = self.snake[-1]
        if head not in self.food:
            self.board[self.snake[0][0]][self.snake[0][1]] = EMPTY
            self.snake.pop(0)
        else:
            self.food.remove(head)

        # check out of bounds
        head = self.snake[-1]
        if (
                head[0] >= self.size
                or head[1] >= self.size
                or head[0] < 0
                or head[1] < 0

        ):
            self.should_terminate = True
        else:
            self.board[head[0]][head[1]] = 1

        # spawn new food
        while len(self.food) < self.num_food:
            x = self.food_xy[self.food_index][0]
            y = self.food_xy[self.food_index][1]
            while self.board[x][y] != EMPTY:
                self.food_index += 1
                x = self.food_xy[self.food_index][0]
                y = self.food_xy[self.food_index][1]
            self.food.append((x, y))
            self.board[x][y] = FOOD
            self.food_index += 1
        return move

    def play(self, display):
        if display:
            self.display_board()
        while True:
            if self.should_terminate:
                return 0
            if self.turn >= self.max_turns:
                return 0
            moves = self.move()
            self.turn += 1
            if display:
                for move in moves:
                    if move == UP:
                        print("UP")
                    elif move == DOWN:
                        print("DOWN")
                    elif move == LEFT:
                        print("LEFT")
                    elif move == RIGHT:
                        print("RIGHT")
                self.display_board()
                if self.gui is not None:
                    self.gui.update()
                time.sleep(0.5)

    def display_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == EMPTY:
                    print("|_", end="")
                elif self.board[i][j] == FOOD:
                    print("|#", end="")
                else:
                    print("|" + str(int(self.board[i][j])), end="")
            print("|")


class Gui:
    def __init__(self, game, size):
        self.game = game
        self.game.gui = self
        self.size = size

        self.ratio = (self.size / self.game.size)*50

        self.app = tk.Tk()
        self.canvas = tk.Canvas(self.app, width=self.size*50, height=self.size*50)
        self.canvas.pack()

        for i in range(len(self.game.snake)):
            color = "#" + "{0:03X}".format((i + 1) * 500)
            snake = self.game.snake
            self.canvas.create_rectangle(
                snake[-1][1] * self.ratio,
                snake[-1][0] * self.ratio,
                (snake[-1][1] + 1) * self.ratio,
                (snake[-1][0] + 1) * self.ratio,
                fill=color,
            )

            for j in range(len(snake) - 1):
                color = "#" + "{0:03X}".format((i + 1) * 123)
                self.canvas.create_rectangle(
                    snake[j][1] * self.ratio,
                    snake[j][0] * self.ratio,
                    (snake[j][1] + 1) * self.ratio,
                    (snake[j][0] + 1) * self.ratio,
                    fill=color,
                )

        for food in self.game.food:
            self.canvas.create_rectangle(
                food[1] * self.ratio,
                food[0] * self.ratio,
                (food[1] + 1) * self.ratio,
                (food[0] + 1) * self.ratio,
                fill="#000000000",
            )

    def update(self):
        self.canvas.delete("all")
        color = "#" + "{0:03X}".format(500)
        snake = self.game.snake
        self.canvas.create_rectangle(
            snake[-1][1] * self.ratio,
            snake[-1][0] * self.ratio,
            (snake[-1][1] + 1) * self.ratio,
            (snake[-1][0] + 1) * self.ratio,
            fill=color,
        )

        for j in range(len(snake) - 1):
            color = "#" + "{0:03X}".format(123)
            self.canvas.create_rectangle(
                snake[j][1] * self.ratio,
                snake[j][0] * self.ratio,
                (snake[j][1] + 1) * self.ratio,
                (snake[j][0] + 1) * self.ratio,
                fill=color,
            )

        for food in self.game.food:
            self.canvas.create_rectangle(
                food[1] * self.ratio,
                food[0] * self.ratio,
                (food[1] + 1) * self.ratio,
                (food[0] + 1) * self.ratio,
                fill="#000000000",
            )

        self.canvas.pack()
        self.app.update()
