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
        if method == 'backtracking':
            for x in self.connected_states:
                x.domain.removeColor(color)
                x.constraining=x.constraining-1
        else:
            self.domain.removeColor(color)

    def updateSurroundingColors(self) -> bool:
        changed = False
        for s in self.connected_states + [self]:
            original_colors = [x for x in s.domain.available_colors]
            s.domain.available_colors = [x for x in s.domain.initial_colors]
            colors_to_remove: List[str] = []
            for color in s.domain.available_colors:
                for c in s.connected_states:
                    if c.color == color:
                        colors_to_remove.append(color)

            for color in colors_to_remove:
                s.domain.removeColor(color)

            if s.domain.available_colors != original_colors:
                changed = True

        return changed

    def __repr__(self):
        return "State: " + self.name + ", Color: " + self.color + ", Connected states: " + \
               str([x.name for x in self.connected_states]) + ", Domain: " + str(self.domain)
