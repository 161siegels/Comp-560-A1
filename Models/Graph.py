from typing import Dict, List

from Models.Edge import Edge
from Models.State import State


class Graph:

    def __init__(self, states, edges):
        self.states: List[State] = states
        self.edges: Dict[str, Edge] = edges

    def __repr__(self):

        output: str = "Graph with states:\n"
        for s in self.states:
            output += "\t" + str(s) + "\n"

        output += "And Edges:\n"
        for k in self.edges.keys():
            output += "\t" + k + ":\n"
            output += "\t" + str(self.edges[k]) + "\n"

        return output
