from game import rand, np, Game
import numpy

window_size = 7
hidden_size = 15
board_size = 10


def generate_brain():
    hidden_layer1 = np.array([
        [rand.uniform(-1, 1) for _ in range(window_size ** 2 + 1)]
        for _ in range(hidden_size)])

    hidden_layer2 = np.array([
        [rand.uniform(-1, 1) for _ in range(hidden_size + 1)]
        for _ in range(hidden_size)])

    output_layer = np.array([
        [rand.uniform(-1, 1) for _ in range(hidden_size + 1)]
        for _ in range(4)])
    return [hidden_layer1, hidden_layer2, output_layer]


# these two in order to represent as float vector for creator

def flatten_brain(brain):
    return numpy.concatenate((brain[0].flatten(), brain[1].flatten(), brain[2].flatten()))


def inflate_brain(arr):
    hidden_layer1 = arr[:750].reshape(15, 50)
    hidden_layer2 = arr[750:(750 + 15 * 16)].reshape(15, 16)
    output_layer = arr[750 + (15 * 16):750 + (15 * 16) + (4 * 16)].reshape(4, 16)
    return [hidden_layer1, hidden_layer2, output_layer]


def evaluate_brain(player):
    game = Game(player)
    game.play(False)
    score = len(game.snake)
    return score


def mutate_brain(brain, mutation_chance, mutation_size):
    new_brain = []
    for layer in brain:
        new_layer = np.copy(layer)
        for i in range(new_layer.shape[0]):
            for j in range(new_layer.shape[1]):
                if rand.uniform(0, 1) < mutation_chance:
                    new_layer[i][j] += rand.uniform(-1, 1) * mutation_size
        new_brain.append(new_layer)
    return new_brain
