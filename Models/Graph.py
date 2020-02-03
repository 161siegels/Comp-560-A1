from typing import Dict, List

from Models.Edge import Edge
from Models.State import State


class Graph:

    def __init__(self, states, edges):
        self.states: List[State] = states
        self.edges: Dict[str, Edge] = edges

    def printColorConnections(self):
        for s in self.states:
            for c in s.connected_states:
                print(s.color + " (" + s.name + ") to " + c.color + " (" + c.name + ")")
        print(self.getIncorrectCount())

    def getIncorrectCount(self):
        sum: int = 0
        for s in self.states:
            if s.color in [c.color for c in s.connected_states if c.color == s.color]:
                sum += 1
        return sum

    def __repr__(self):

        output: str = "Graph with states:\n"
        for s in self.states:
            output += "\t" + str(s) + "\n"

        output += "And Edges:\n"
        for k in self.edges.keys():
            output += "\t" + k + ":\n"
            output += "\t" + str(self.edges[k]) + "\n"

        return output
