from typing import List

from Models.Domain import Domain
import collections


class State:

    def __init__(self, name: str, colors: List[str]):
        self.name: str = name
        self.color: str = ""
        self.domain: Domain = Domain(colors)
        self.connected_states: List[State] = []
        self.constraining: int =0

    #This makes sure that all neighbors are included for each state
    def addConnectedState(self, state):
        if state not in self.connected_states:
            self.connected_states.append(state)
            self.constraining = self.constraining+1
            return True
        else:
            return False

    #This is the assign color method for backtracking search. Takes in a color parameter to
    #assign a particular color for a particular state. Then it iterates through all the states
    #connected to this newly assigned states to remove this color from their domains. If any
    #of the states have not been assigned a color and now have a domain length of 1, it will
    #recursively call this function for that state (and the remaining color in its domain).
    def assignColor(self, color: str,colored_states=[], method='backtracking'):
        self.color = color
        self.domain.removeColor(color)
        if method == 'backtracking':
            if self not in colored_states:
                colored_states.append(self)
            for x in self.connected_states:
                x.domain.removeColor(color)
                if (x.color=='') & (len(x.domain.available_colors) == 1):
                    x.assignColor(x.domain.available_colors[0],colored_states=colored_states)
                x.constraining=x.constraining-1
        else:
            for c in self.connected_states:
                c.updateAvailableColors()

    def getNumberConflicts(self):
        return len([c for c in self.connected_states if c.color == self.color])

    def updateAvailableColors(self):
        colors_to_remove = set()
        for c in self.connected_states:
            colors_to_remove.add(c.color)
        self.domain.available_colors = [x for x in self.domain.initial_colors if x not in list(colors_to_remove)]

    def updateSurroundingColors(self) -> int:
        changes: int = 0
        for s in self.connected_states + [self]:
            original_colors = [x for x in s.domain.available_colors]
            s.domain.available_colors = [x for x in s.domain.initial_colors]
            colors_to_remove: List[str] = []
            for color in s.domain.available_colors:
                for c in s.connected_states:
                    if c.color == color and (color not in colors_to_remove):
                        colors_to_remove.append(color)

            for color in colors_to_remove:
                s.domain.removeColor(color)

            changes += len(list(set(s.domain.available_colors) - set(original_colors)))

        return changes

    def __repr__(self):
        return "State: " + self.name + ", Color: " + self.color + ", Connected states: " + \
               str([x.name for x in self.connected_states]) + ", Domain: " + str(self.domain)
