from typing import List
from Models.Graph import Graph
import random
import pandas as pd


class BacktrackSearch:

    def __init__(self, graph):
        random.seed(123)
        self.graph: Graph = graph
        self.colors: List[str] = self.graph.states[0].domain.initial_colors
        #self.remaining: int = len(self.graph.states)
        self.randomAssign(self.findNextToColor())

    def randomAssign(self,state):
        #visited_nodes=[]
        #visited_nodes.append(to_color)
        curr_state=state
        next_state=self.findNextToColor()
        for x in curr_state.domain.initial_colors:
            if x in curr_state.domain.available_colors:
                curr_state.assignColor(x)
                if not self.findNextToColor():
                    return
                self.randomAssign(next_state)
    def findNextToColor(self):
        states = []
        domain_length = []
        empty_neighbors = []
        color = []
        for s in self.graph.states:
            states.append(s)
            color.append(s.color)
            domain_length.append(len(s.domain.available_colors))
            empty_neighbors.append(s.constraining)
        df = pd.DataFrame(list(zip(states, color, domain_length, empty_neighbors)),
                          columns=['states', 'color', 'domain_length', 'empty_neighbors'])
        df = df[df.color == '']
        if df.empty:
            return False
        df = df[df.domain_length == min(df.domain_length)]
        to_color = df[df.empty_neighbors == max(df.empty_neighbors)].iloc[0, 0]
        return to_color

    def __repr__(self):
        return str(self.graph)
