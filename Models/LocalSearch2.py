import random
import copy
import time
import sys
from typing import List

from Models.Graph import Graph
from Models.Result import Result


class LocalSearch2:

    def __init__(self, graph):
        self.INITIAL_GRAPH = graph
        self.SECONDS_TO_RUN = 60
        self.graph: Graph = self.INITIAL_GRAPH
        self.colors: List[str] = self.graph.states[0].domain.initial_colors
        self.violations_to_beat = sys.maxsize
        self.result = Result()
        self.steps = 0
        self.total_steps = 0
        self.restarts = 0

    # This implementation of local search randomly assigns each state a color, then iterates through each state,
    # assigning a new color if it lowers the total number of constraint violations and skipping otherwise until
    # it either begins the loop again and continues doing the same or totally restarts by assigning a random new color
    # to every state. The details for how this decision is made can be found in the comments below.
    def search(self):
        self.randomAssign()
        t_start = time.time()

        # runs for 1 minute
        while time.time() < t_start + self.SECONDS_TO_RUN:
            current_results = self.changeRandomState((t_start + self.SECONDS_TO_RUN) - time.time())

            # Terminates if the optimal solution has been found, runs through each state again
            # if improvement has been made, randomly assigns all new colors if the state space has gotten worse.
            if current_results.violations == 0:
                self.setViolationsToBeat(current_results)
                break
            elif self.result.violations <= current_results.violations:
                self.setViolationsToBeat(current_results)
            else:
                self.resetSteps()
                self.randomAssign()
        print("\nBest matches:\n" + self.result.graph.printColorConnections())
        print("Violations: " + str(self.result.violations))
        print("Restarts: " + str(self.restarts))
        print("Steps taken during best iteration: " + str(self.result.steps))
        print("Total steps: " + str(self.total_steps))

    # Randomly shuffles states, then iterates through each one. At each state, we randomly assign it a color.
    # We then check to see if this has produced more constraint violations, if so we put the color back how it was
    # and move on to the next state. If the new color produces fewer constraint violations, we keep the new color
    # for that state and notify the connected states that they should remove it from the list of random colors they
    # can be assigned to. As we continue this process, we check each time we are about to iterate whether there
    # are zero constraint violations, in which case we terminate.
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
                    self.incrementSteps()

            violations = self.calculateViolatedConstraints(new_graph)
            if violations == 0:
                break

        return Result(violations, new_graph, self.steps)

    def incrementSteps(self):
        self.steps += 1
        self.total_steps += 1

    # Updates the best result found so far
    def setViolationsToBeat(self, result):
        self.violations_to_beat = result.violations
        if self.result.violations > result.violations:
            self.result = result

    # Randomly assigns every state a color
    def randomAssign(self):
        for s in self.graph.states:
            colors = s.domain.initial_colors
            curr_color = random.choice(colors)
            s.color = curr_color
        self.setViolationsToBeat(Result(self.calculateViolatedConstraints(self.graph), self.graph, 0))
        self.restarts += 1

    # Calculates how many connected states share the same color
    def calculateViolatedConstraints(self, graph: Graph):
        violations = 0
        for s in graph.states:
            for c in s.connected_states:
                if s.color == c.color:
                    violations += 1
        return violations

    def resetSteps(self):
        self.steps = 0
