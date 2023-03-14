# ECSnake
Evolutionary Computing project built in Java.
6
The Code
Our project contains 6 files:
• game.py
• genetic_operators.py
• genetic_players.py
• main.py
• utils.py
• run.py.
We will layout the main functions and purpose of each file.
• Utils.py:
This file contains various functions for the overall functionality of the project.
These functions are as follows:
o generate_brain() – this generates a randomly initiated neural network
with two hidden layers.
o flatten_brain(brain) – takes a brain and returns a single vector of the
concatenated brain layers.
o inflate_brain(arr) – reverses flatten_brain.
o evaluate_brain(player) – plays a game with player controlling the snake.
Returns the final length of the snake upon termination.
o mutate_brain(brain, mutation_chance, mutation_size) –
creates a new brain based on the given brain. For each element in brain
the chance of it changing is mutation chance and it can change up to
mutation_size in either direction.
• Game.py:
This file contains the implementation of the game itself. The class Game receives
a player object.
o Class Game:
▪ Constructor: initializer of the game, receives a player (brain) and
sets up all the required fields.
▪ Move() – Calls the next_move method of genetic_player and
updates the board accordingly.
▪ Play() – Stimulates the game iterations.
7
o Class GUI: defines and runs GUI.
• Genetic_player.py:
Here we implement an individual neural network for the snake agents.
o Constructor: receives brain and initializes the player.
o Process_board(board, snake): receives the board current instance,
processes it giving priority to squares with food and negative priority to
squares with snake's body or game border.
o Next_move(board, snake): Calls process_board and propagates the
results through the brain matrices, returns the max value of final layer (4
float values representing UP DOWN LEFT RIGHT)
• Genetic_operators.py:
Contains operators used for EC-Kity and the project.
o Class BrainCreator – Creates an individual for the ECKity population.
o Class BrainEvaluator – Evaluates an individual by running a game instance
on a given brain.
o Class BrainMutator(mutate_chance) – Mutates an individual with
consideration of mutate_chance by adding or decreasing values in an
individual brain, each cell is randomly mutated.
o Class BrainCross(cross_chance) – Crosses two brains by splicing them
randomly, with consideration of cross_chance.
• Main.py:
Initiates the ECKity main algorithm.
Sets the SimpleEvolution and runs it.
• Run.py:
Runs an instance of the game with given individual (brain).
