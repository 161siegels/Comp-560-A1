import sys


class Result:

    def __init__(self, violations=sys.maxsize, graph=None, steps=sys.maxsize):
        self.violations = violations
        self.graph = graph
        self.steps = steps
