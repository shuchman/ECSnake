from eckity.creators.ga_creators.simple_vector_creator import GAVectorCreator
from eckity.genetic_encodings.ga.float_vector import FloatVector
from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
from eckity.genetic_operators.genetic_operator import GeneticOperator
from genetic_player import GeneticPlayer
from utils import *

window_size = 7
hidden_size = 15
board_size = 10


class BrainCreator(GAVectorCreator):
    def __init__(self,
                 length=1,
                 events=None):
        super().__init__(length, None, (-1, 1), FloatVector, events)

    def create_vector(self, individual):
        flattened_brain = flatten_brain(generate_brain())
        individual.set_vector(flattened_brain)


class BrainEvaluator(SimpleIndividualEvaluator):
    def __init__(self):
        super().__init__()

    def _evaluate_individual(self, individual):
        brain = inflate_brain(individual.get_vector())
        player = GeneticPlayer(brain)
        game = Game(player)
        game.play(False)
        score = len(game.snake)
        return score


class BrainMutator(GeneticOperator):
    def __init__(self, probability):
        super().__init__(arity=1, probability=probability)
        self.applied_individuals = None

    def apply(self, individuals):
        for individual in individuals:
            flattened = individual.get_vector()
            inflated = inflate_brain(flattened)
            mutated = mutate_brain(inflated, self.probability, 0.3)
            individual.set_vector(flatten_brain(mutated))
        self.applied_individuals = individuals
        return individuals


class BrainCross(GeneticOperator):
    def __init__(self, probability):
        self.applied_individuals = None
        super().__init__(arity=2, probability=probability)

    def apply(self, individuals):
        for i in range(0, len(individuals) - 1, 2):
            if i + 1 < len(individuals):
                individuals[i], individuals[i + 1] = self.cross(individuals[i], individuals[i + 1])
        self.applied_individuals = individuals
        return individuals

    def cross(self, individual1, individual2):
        save = [0 for _ in range(1054)]
        vec1 = individual1.get_vector()
        vec2 = individual2.get_vector()
        start_index = rand.randint(0, 1054)
        end_point = max(start_index, rand.randint(0, 1054))
        for i in range(start_index, end_point):
            save[i] = vec1[i]
            vec1[i] = vec2[i]
            vec2[i] = save[i]
        individual1.set_vector(vec1)
        individual2.set_vector(vec2)
        return individual1, individual2


