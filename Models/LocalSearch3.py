import random
import copy
import time
import sys
from collections import deque
from typing import List

from Models.Graph import Graph


class LocalSearch3:

    # to do: add random restarts

    def __init__(self, graph):
        self.SECONDS_TO_RUN = 60
        self.graph: Graph = graph
        self.colors: List[str] = self.graph.states[0].domain.initial_colors
        self.steps = 0
        self.steps_since_last_restart = 0
        self.restarts = 0
        self.queue = deque(maxlen=len(self.colors) + 1)

    def search(self):
        self.randomAssign()
        self.restarts = 0
        t_start = time.time()
        completed = False

        # runs for 1 minute
        while time.time() < t_start + self.SECONDS_TO_RUN:
            most_conflicted_state = self.findMostConflictedState()
            color_conflicts = self.fixConflictedState(most_conflicted_state)
            most_conflicted_state["state"].color = color_conflicts["color"]
            self.incrementSteps()
            total_violations = self.calculateViolatedConstraints(self.graph)

            if total_violations == 0:
                completed = True
                break

            if (len(list(set(self.queue))) <= 2 and len(self.queue) == self.queue.maxlen) or \
                    self.steps_since_last_restart % 1000 == 0:
                self.randomAssign()

            self.queue.append(most_conflicted_state["state"].name)

        if completed:
            print("States:\n" + self.graph.printStateColors())
            print("Local Search completed with " + str(self.calculateViolatedConstraints(self.graph)) +
                  " connected states of the same color.")
            print("Random reassigns: " + str(self.restarts))
            print("Total steps: " + str(self.steps))
            print("Steps taken since last random reassign: " + str(self.steps_since_last_restart))
        else:
            print("Could not find optimal solution with local search.")

    def fixConflictedState(self, most_conflicted):
        # In the form { number_of_conflicts: [list of colors resulting in that many conflicts] }
        conflict_color_map = {}

        for c in most_conflicted["state"].domain.initial_colors:
            new_graph = copy.deepcopy(self.graph)
            new_state = [x for x in new_graph.states if x.name == most_conflicted["state"].name][0]
            new_state.color = c
            violated_constraints = self.calculateViolatedConstraints(new_graph)

            if violated_constraints in conflict_color_map.keys():
                conflict_color_map[violated_constraints] += [c]
            else:
                conflict_color_map[violated_constraints] = [c]

        least_conflicts = min(conflict_color_map.keys())
        chosen_color = random.choice(conflict_color_map[least_conflicts])

        return {
            "color": chosen_color,
            "conflicts": least_conflicts
        }

    # Searches through the graph and returns the state with the most constraint violations
    def findMostConflictedState(self):
        # In the form { number_of_conflicts: [list of states with that many conflicting connections] }
        conflict_state_map = {}

        for s in self.graph.states:
            conflicts = s.getNumberConflicts()

            if conflicts in conflict_state_map.keys():
                conflict_state_map[conflicts] += [s]
            else:
                conflict_state_map[conflicts] = [s]

        most_conflicts = max(conflict_state_map.keys())
        chosen_state = random.choice(conflict_state_map[most_conflicts])

        return {
            "state": chosen_state,
            "conflicts": most_conflicts
        }

    def incrementSteps(self):
        self.steps += 1
        self.steps_since_last_restart += 1

    # Randomly assigns every state a color
    def randomAssign(self):
        for s in self.graph.states:
            s.color = random.choice(self.colors)
        self.restarts += 1
        self.steps_since_last_restart = 0

    # Calculates how many connected states share the same color
    def calculateViolatedConstraints(self, graph: Graph):
        violations = 0
        for s in graph.states:
            for c in s.connected_states:
                if s.color == c.color:
                    violations += 1
        return violations
