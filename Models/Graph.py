from typing import Dict, List

from Models.Edge import Edge
from Models.State import State


class Graph:

    def __init__(self, states, edges):
        self.states: List[State] = states
        self.edges: Dict[str, Edge] = edges

    #prints the colors of each state in a given edge. Prints number of violations
    def printColorConnections(self):
        output: str = ""
        for s in self.states:
            for c in s.connected_states:
                output += s.color + " (" + s.name + ") to " + c.color + " (" + c.name + ")\n"
        return output

    #prints the color of each state
    def printStateColors(self):
        output = ""
        for s in self.states:
            output += s.name + " - " + s.color + "\n"
        return output

    def __repr__(self):

        output: str = "Graph with states:\n"
        for s in self.states:
            output += "\t" + str(s) + "\n"

        output += "And Edges:\n"
        for k in self.edges.keys():
            output += "\t" + k + ":\n"
            output += "\t" + str(self.edges[k]) + "\n"

        return output
