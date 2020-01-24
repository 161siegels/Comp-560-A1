class State:

    def __init__(self, name):
        self.name = name
        self.color = ""
        self.connected_states = []

    def addConnectedState(self, state):
        if state not in self.connected_states:
            self.connected_states.append(state)
            return True
        else:
            return False

    def __repr__(self):
        return "State: " + self.name + ", Color: " + self.color + ", Connected states: " + \
               str([x.name for x in self.connected_states])
