import random
import copy
import time
import sys
from typing import List

from Models.Graph import Graph
from Models.Result import Result


class LocalSearch3:

    # to do: delete while break, remove seed, make list of tied best colors and pick one randomly
    # add random restarts

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

    def search(self):
        self.randomAssign()
        t_start = time.time()
        random.seed(123)
        i = 0

        # runs for 1 minute
        while time.time() < t_start + self.SECONDS_TO_RUN:
            most_conflicted_state = self.findMostConflictedState()
            color_conflicts = self.fixConflictedState(most_conflicted_state)
            most_conflicted_state["state"].color = color_conflicts["color"]
            self.incrementSteps()
            total_violations = self.calculateViolatedConstraints(self.graph)
            self.violations_to_beat = total_violations
            print(total_violations)
            if self.calculateViolatedConstraints(self.graph) == 0:
                break

        print("\nBest matches:\n" + self.result.graph.printColorConnections())
        print("Violations: " + str(self.result.violations))
        print("Restarts: " + str(self.restarts))
        print("Steps taken during best iteration: " + str(self.steps))
        print("Total steps: " + str(self.total_steps))

    def fixConflictedState(self, most_conflicted):
        conflict_color_map = {}

        print("Most conflicted before: " + str(most_conflicted))
        for c in most_conflicted["state"].domain.initial_colors:
            new_graph = copy.deepcopy(self.graph)
            new_state = [x for x in new_graph.states if x.name == most_conflicted["state"].name][0]
            print("Before color change: " + new_state.name + " has color " + new_state.color + \
                  " and there are " + str(self.calculateViolatedConstraints(new_graph)) + " conflicts")
            new_state.color = c
            violated_constraints = self.calculateViolatedConstraints(new_graph)
            if violated_constraints in conflict_color_map.keys():
                conflict_color_map[violated_constraints] += [c]
            else:
                conflict_color_map[violated_constraints] = [c]
            print("Now: " + new_state.name + " has color " + new_state.color + \
                  " and there are " + str(self.calculateViolatedConstraints(new_graph)) + " conflicts")
        lowest_key = min(conflict_color_map.keys())
        chosen_color = random.choice(conflict_color_map[lowest_key])

        print("Most conflicted after: " + str(most_conflicted))
        return {
            "color": chosen_color,
            "conflicts": lowest_key
        }

    # Searches through the graph and returns the state with the most constraint violations
    def findMostConflictedState(self):
        conflict_state_map = {}
        for s in self.graph.states:
            conflicts = s.getNumberConflicts()
            if conflicts in conflict_state_map.keys():
                conflict_state_map[conflicts] += [s]
            else:
                conflict_state_map[conflicts] = [s]
        highest_key = max(conflict_state_map.keys())
        chosen_state = random.choice(conflict_state_map[max(conflict_state_map.keys())])
        return {
            "state": chosen_state,
            "conflicts": highest_key
        }

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
