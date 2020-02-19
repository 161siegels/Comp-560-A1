from typing import List
from Models.Graph import Graph
import random
import pandas as pd


class BacktrackSearch:

    def __init__(self, graph):
        random.seed(123)
        self.graph: Graph = graph
        self.numSteps: int = 0
        self.numLeft: int = len(graph.states)
        self.execute(self.findNextToColor())

    #Runs the backtracking search. Calls function to color the state given in the parameter. Calls function
    #to find the next state to color and then calls the function to color that state with one of the colors
    #in its domain. Uses a for loop and recursive function call to call this method until there are no uncolored
    #states left
    def execute(self, state):
        curr_state = state
        for x in curr_state.domain.available_colors:
            if self.numLeft == 0:
                return
            elif x in curr_state.domain.available_colors:
                self.numSteps = 1 + self.numSteps
                self.numLeft = curr_state.assignColor(x,left=self.numLeft)
                next_state=self.findNextToColor()
                if not next_state:
                    return
                self.execute(next_state)

    #Finds the next state to color by searching for a state that has not yet been colored and has the
    #minimum domain length. It breaks ties by choosing the state with the maximum number of empty neighbors.
    #Returns the state to be colored
    def findNextToColor(self):
        states = []
        domain_length = []
        empty_neighbors = []
        color = []
        for s in self.graph.states:
            states.append(s)
            color.append(s.color)
            domain_length.append(len(s.domain.available_colors))
            empty_neighbors.append(s.constraining)
        df = pd.DataFrame(list(zip(states, color, domain_length, empty_neighbors)),
                          columns=['states', 'color', 'domain_length', 'empty_neighbors'])
        df = df[df.color == '']
        if df.empty:
            return False
        df = df[df.domain_length == min(df.domain_length)]
        to_color = df[df.empty_neighbors == max(df.empty_neighbors)].iloc[0, 0]
        return to_color

    #Prints the states colors and the number of steps needed to solve the search
    def __repr__(self):
        self.graph.printStateColors()
        return "Number of steps needed to solve: " + str(self.numSteps)
