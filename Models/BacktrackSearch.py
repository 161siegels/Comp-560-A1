from typing import List
from Models.Graph import Graph
import random
import pandas as pd


class BacktrackSearch:

    def __init__(self, graph):
        random.seed(123)
        self.graph: Graph = graph
        self.colors: List[str] = self.graph.states[0].domain.initial_colors
        self.remaining: int = len(self.graph.states)
        self.randomAssign()

    def randomAssign(self):
        visited_nodes=[]
        states=[]
        domain_length=[]
        empty_neighbors=[]
        color=[]
        for s in self.graph.states:
            states.append(s)
            color.append(s.color)
            domain_length.append(len(s.domain.available_colors))
            empty_neighbors.append(s.constraining)
        df=pd.DataFrame(list(zip(states,color, domain_length,empty_neighbors)), columns =['states','color' ,'domain_length','empty_neighbors'])
        df=df[df.color=='']
        df=df[df.domain_length==min(df.domain_length)]

        to_color=df[df.empty_neighbors==max(df.empty_neighbors)].iloc[0,0]
        visited_nodes.append(to_color)
        print(to_color)

    def __repr__(self):
        return str(self.graph)
