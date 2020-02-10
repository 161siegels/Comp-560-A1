from typing import List
from Models.Graph import Graph
from Models.staticHelpers import printProgress
import random
import time
import sys


class LocalSearch:

    def __init__(self, graph, seed: int):
        self.INITIAL_SEED = seed
        self.INITIAL_GRAPH = graph
        self.graph: Graph = self.INITIAL_GRAPH
        self.colors: List[str] = self.graph.states[0].domain.initial_colors

    def localSearchController(self):
        iterations_per_dot: int = 1000
        print("Beginning localsearch (each dot represents " + str(iterations_per_dot) + " iterations):")
        i: int = 0
        min_conflicts: int = sys.maxsize
        best_combination: str = ""

        t_start = time.time()
        t_end = t_start + 60

        while time.time() < t_end:
            self.graph = self.INITIAL_GRAPH
            random.seed(self.INITIAL_SEED + i)
            self.randomAssign()
            conflicts: int = self.correctColors()
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                best_combination = self.graph.printColorConnections()

            printProgress(i, iterations_per_dot)
            if conflicts == 0:
                break
            i += 1

        print("\nIt took " + str(i) + " iterations to find the following combination with " + str(min_conflicts) + " conflicts:" + "\n" + best_combination)

    def randomAssign(self):
        for s in self.graph.states:
            colors = s.domain.initial_colors
            curr_color = random.choice(colors)
            s.color = curr_color

    def correctColors(self) -> int:

        iterations = 0

        while True:
            changed: bool = False
            for s in self.graph.states:
                connected_colors: List[str] = [x.color for x in s.connected_states]
                if s.color not in connected_colors:
                    continue
                else:
                    for c in s.domain.available_colors:
                        if c not in connected_colors:
                            changed = True
                            s.assignColor(c)
                            break

                    if s.updateSurroundingColors():
                        changed = True
                
            iterations += 1

            if (not changed) or iterations >= 1000:
                break

        return self.graph.getIncorrectCount()

    def __repr__(self):
        return str(self.graph)
