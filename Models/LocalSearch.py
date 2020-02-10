from typing import List
from Models.Graph import Graph
import random
import time


class LocalSearch:

    def __init__(self, graph, seed: int):
        self.INITIAL_SEED = seed
        self.INITIAL_GRAPH = graph
        self.graph: Graph = self.INITIAL_GRAPH
        self.colors: List[str] = self.graph.states[0].domain.initial_colors

    def localSearchController(self):
        t_end = time.time() + 60
        i: int = 0
        while time.time() < t_end:
            self.graph = self.INITIAL_GRAPH
            random.seed(self.INITIAL_SEED + i)
            self.randomAssign()
            conflicts: int = self.correctColors()
            print("Conflicts on iteration " + str(i) + ": " + str(conflicts) + "\n")
            if conflicts == 0:
                break
            i += 1
        self.graph.printColorConnections()

    def randomAssign(self):
        for s in self.graph.states:
            colors = s.domain.initial_colors
            curr_color = random.choice(colors)
            s.color = curr_color

        print("initial incorrect: " + str(self.graph.getIncorrectCount()))

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
