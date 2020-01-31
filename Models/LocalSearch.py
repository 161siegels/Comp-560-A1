from typing import List
from Models.Graph import Graph
import random


class LocalSearch:

    def __init__(self, graph):
        random.seed(123)
        self.graph: Graph = graph
        self.colors: List[str] = self.graph.states[0].domain.initial_colors
        self.randomAssign()

    def randomAssign(self):
        for s in self.graph.states:
            colors = s.domain.available_colors
            curr_color = random.choice(colors)
            s.assignColor(curr_color)

    def __repr__(self):
        return str(self.graph)
