from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation

#Didya code:
import pandas as pd
import openpyxl

from genetic_operators import BrainCreator, BrainMutator, BrainEvaluator, BrainCross
from genetic_player import GeneticPlayer
from utils import inflate_brain

from game import Game

algo = SimpleEvolution(
    Subpopulation(creators=BrainCreator(),
                  population_size=10, #40,
                  evaluator=BrainEvaluator(),
                  higher_is_better=True,
                  elitism_rate=0.0,
                  operators_sequence=[
                      BrainCross(probability=0.0),#0.1
                      BrainMutator(probability=0.2),#0.5
                  ],
                  selection_methods=[
                      (TournamentSelection(tournament_size=4, higher_is_better=True), 1)
                  ]),
    breeder=SimpleBreeder(),
    max_workers=5,
    max_generation=10000,
    statistics=BestAverageWorstStatistics()
)

algo.evolve()
res = algo.execute()

#Didya code:
df = pd.DataFrame(res)
df.to_excel('res_brain.xlsx', index=False, header=False)

player = GeneticPlayer(inflate_brain(res))
game = Game(player, gui=True)
game.play(True)
print(res)
