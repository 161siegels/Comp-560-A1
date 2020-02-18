import random
import copy
import time
import sys
from typing import List

from Models.Graph import Graph
from Models.OutputWriter import OutputWriter
from Models.Result import Result


class LocalSearch2:

    def __init__(self, graph, seed: int, file_name: str):
        self.INITIAL_GRAPH = graph
        self.SECONDS_TO_RUN = 60
        self.graph: Graph = self.INITIAL_GRAPH
        self.colors: List[str] = self.graph.states[0].domain.initial_colors
        self.violations_to_beat = sys.maxsize
        self.result = Result()
        self.steps = 0

    def search(self):
        self.randomAssign()
        t_start = time.time()

        while time.time() < t_start + self.SECONDS_TO_RUN:
            # print("Changing a random state")
            current_results = self.changeRandomState((t_start + self.SECONDS_TO_RUN) - time.time())
            if current_results.violations == 0:
                self.setViolationsToBeat(current_results)
                break
            elif self.result.violations <= current_results.violations:
                self.setViolationsToBeat(current_results)
            else:
                print("Number of violations increased, starting over")
                self.resetSteps()
                self.randomAssign()
            # print("New amount of violated constraints: " + str(self.violations_to_beat))
        print("\nBest matches:\n" + self.result.graph.printColorConnections())
        print("Violations: " + str(self.result.violations))
        print("Steps: " + str(self.result.steps))

    def changeRandomState(self, time_left) -> Result:
        violations = sys.maxsize
        t_start = time.time()
        new_graph = copy.deepcopy(self.graph)
        states = new_graph.states
        random.shuffle(states)
        state_iterator = iter(states)

        while (violations >= self.violations_to_beat) and \
              ((time.time() - t_start) < time_left):

            try:
                state = next(state_iterator)
            except StopIteration:
                break

            if len(state.domain.available_colors) > 0:
                current_violations = self.calculateViolatedConstraints(new_graph)
                original_color = state.color
                random_color = random.choice(state.domain.available_colors)
                state.assignColor(random_color)
                if self.calculateViolatedConstraints(new_graph) > current_violations:
                    state.assignColor(original_color)
                else:
                    self.steps += 1

            violations = self.calculateViolatedConstraints(new_graph)
            if violations == 0:
                break

        return Result(violations, new_graph, self.steps)

    def setViolationsToBeat(self, result):
        self.violations_to_beat = result.violations
        if self.result.violations > result.violations:
            self.result = result

    def randomAssign(self):
        # print("Random assigning...")
        for s in self.graph.states:
            colors = s.domain.initial_colors
            curr_color = random.choice(colors)
            s.color = curr_color
        self.setViolationsToBeat(Result(self.calculateViolatedConstraints(self.graph), self.graph, 0))
        # print("Amount of violated constraints after random assign: " + str(self.violations_to_beat))

    def calculateViolatedConstraints(self, graph: Graph):
        violations = 0
        for s in graph.states:
            for c in s.connected_states:
                if s.color == c.color:
                    violations += 1
        return violations

    def resetSteps(self):
        self.steps = 0
