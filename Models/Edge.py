class Edge:

    def __init__(self, state1, state2):
        self.state1 = state1
        self.state2 = state2

    def __repr__(self):
        return "Edge from " + str(self.state1.name) + " to " + str(self.state2.name)
