from typing import List
from Models.Graph import Graph
import random


class LocalSearch:

    def __init__(self, graph):
        random.seed(123)
        self.graph: Graph = graph
        self.colors: List[str] = self.graph.states[0].domain.initial_colors
        self.randomAssign()
        print("Original-------------")
        self.graph.printColorConnections()
        print("New-------------------")
        self.correctColors(iterations=0)

    def randomAssign(self):
        for s in self.graph.states:
            colors = s.domain.available_colors
            curr_color = random.choice(colors)
            s.assignColor(curr_color)

    def correctColors(self, iterations: int):

        iterations = 0

        while True:
            changed: bool = False
            bad_state = False

            for s in self.graph.states:
                connected_colors: List[str] = [x.color for x in s.connected_states]
                if s.color not in connected_colors:
                    continue
                else:
                    for c in s.domain.available_colors:

                        if c not in connected_colors:
                            changed = True
                            s.color = c
                            break
                        bad_state = True

            print("iterations: " + str(iterations))
            iterations += 1

            if (not changed and not bad_state) or iterations >= 1000:
                break

    def __repr__(self):
        return str(self.graph)
