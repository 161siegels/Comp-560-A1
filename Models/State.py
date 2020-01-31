from typing import List

from Models.Domain import Domain


class State:

    def __init__(self, name: str, colors: List[str]):
        self.name: str = name
        self.color: str = ""
        self.domain: Domain = Domain(colors)
        self.connected_states: List[State] = []

    def addConnectedState(self, state):
        if state not in self.connected_states:
            self.connected_states.append(state)
            return True
        else:
            return False

    def __repr__(self):
        return "State: " + self.name + ", Color: " + self.color + ", Connected states: " + \
               str([x.name for x in self.connected_states]) + ", Domain: " + str(self.domain)
