from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
import numpy

#Didya code:
import pandas as pd
import openpyxl

from genetic_operators import BrainCreator, BrainMutator, BrainEvaluator, BrainCross
from genetic_player import GeneticPlayer
from utils import inflate_brain

from game import Game

print("hi")

excel_data_df = pd.read_excel('res_brain.xlsx', header = None)
res = excel_data_df.values.tolist()

print(res)
res = numpy.array([x for [x] in res])
print(res.shape)
player = GeneticPlayer(inflate_brain(res))
game = Game(player, gui=True)
game.play(True)