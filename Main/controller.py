from Models.State import State


class Controller:

    def __init__(self, input):
        self.input = input
        self.states = []

    def organizeInput(self):

        for s in self.input["states"]:
            self.states.append(State(s))

        for c in self.input["connections"]:
            s1 = c.split(" ")[0]
            s2 = c.split(" ")[1]
            if len([x for x in self.states if x.name == s1]) > 0 and \
               len([x for x in self.states if x.name == s2]) > 0:
                self.connectStates(s1, s2)
            else:
                if len([x for x in self.states if x.name == s1]) == 0:
                    self.states.append(State(s1))
                if len([x for x in self.states if x.name == s2]) == 0:
                    self.states.append(State(s2))
                self.connectStates(s1, s2)

        return self.states

    def connectStates(self, s1, s2):
        first_connected_state = [x for x in self.states if x.name == s1][0]
        second_connected_state = [x for x in self.states if x.name == s2][0]
        first_connected_state.addConnectedState(second_connected_state)
        second_connected_state.addConnectedState(first_connected_state)