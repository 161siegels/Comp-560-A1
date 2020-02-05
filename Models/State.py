from typing import List

from Models.Domain import Domain


class State:

    def __init__(self, name: str, colors: List[str]):
        self.name: str = name
        self.color: str = ""
        self.domain: Domain = Domain(colors)
        self.connected_states: List[State] = []
        self.constraining: int =0

    def addConnectedState(self, state):
        if state not in self.connected_states:
            self.connected_states.append(state)
            self.constraining = self.constraining+1
            return True
        else:
            return False

    def assignColor(self, color: str, method='backtracking'):
        self.color = color
        self.domain.removeColor(color)
        if method == 'backtracking':
            for x in self.connected_states:
                x.domain.removeColor(color)
                if (x.color=='') & (len(x.domain.available_colors) == 1):
                    x.assignColor(x.domain.available_colors[0])
                x.constraining=x.constraining-1
        else:
            self.domain.removeColor(color)

    def __repr__(self):
        return "State: " + self.name + ", Color: " + self.color + ", Connected states: " + \
               str([x.name for x in self.connected_states]) + ", Domain: " + str(self.domain)
