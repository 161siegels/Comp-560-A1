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
    def assignColor(self, color: str,colored_states=[]):
        self.color = color
        self.domain.removeColor(color)
        if self not in colored_states:
            colored_states.append(self)
        for x in self.connected_states:
            x.domain.removeColor(color)
            if (x.color=='') & (len(x.domain.available_colors) == 1):
                x.assignColor(x.domain.available_colors[0],colored_states=colored_states)
            x.constraining=x.constraining-1

    # Returns the number of connected states with the same color
    def getNumberConflicts(self):
        return len([c for c in self.connected_states if c.color == self.color])

    def __repr__(self):
        return "State: " + self.name + ", Color: " + self.color + ", Connected states: " + \
               str([x.name for x in self.connected_states]) + ", Domain: " + str(self.domain)
