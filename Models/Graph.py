from typing import Dict, List

from Models.Edge import Edge
from Models.State import State


class Graph:

    def __init__(self, states, edges):
        self.states: List[State] = states
        self.edges: Dict[str, Edge] = edges

    #prints the colors of each state in a given edge. Prints number of violations
    def printColorConnections(self):
        for s in self.states:
            for c in s.connected_states:
                print(s.color + " (" + s.name + ") to " + c.color + " (" + c.name + ")")
        print(self.getIncorrectCount())

    #prints the color of each state
    def printStateColors(self):
        for s in self.states:
            print(s.color + " (" + s.name + ")")

    #prints the number of edges violated
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
