from Models.State import State


class Edge:

    def __init__(self, state1: State, state2: State):
        self.state1: State = state1
        self.state2: State = state2

    def __repr__(self):
        return "Edge from " + str(self.state1.name) + " to " + str(self.state2.name)
