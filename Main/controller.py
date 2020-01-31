from typing import Dict, List

from Models.Graph import Graph
from Models.State import State
from Models.Edge import Edge


class Controller:

    def __init__(self, input: str):
        self.input = input
        self.states = []
        self.edges = {}

    def organizeInput(self) -> Graph:

        for s in self.input["states"]:
            self.states.append(State(s, self.input["colors"]))

        for c in self.input["connections"]:
            s1 = c.split(" ")[0]
            s2 = c.split(" ")[1]
            if len([x for x in self.states if x.name == s1]) > 0 and \
               len([x for x in self.states if x.name == s2]) > 0:
                self.connectStates(s1, s2)
            else:
                if len([x for x in self.states if x.name == s1]) == 0:
                    self.states.append(State(s1, self.input["colors"]))
                if len([x for x in self.states if x.name == s2]) == 0:
                    self.states.append(State(s2, self.input["colors"]))
                self.connectStates(s1, s2)

        for s in self.states:
            if len(s.connected_states) > 0:
                for c in s.connected_states:
                    if c.name in self.edges.keys():
                        self.edges[c.name].append(Edge(c, s))
                    else:
                        self.edges[c.name] = [Edge(c, s)]

        return Graph(self.states, self.edges)


    def connectStates(self, s1, s2):
        first_connected_state = [x for x in self.states if x.name == s1][0]
        second_connected_state = [x for x in self.states if x.name == s2][0]
        first_connected_state.addConnectedState(second_connected_state)
        second_connected_state.addConnectedState(first_connected_state)
