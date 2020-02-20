import random
import copy
import time
from collections import deque
from typing import List
from Models.Graph import Graph


class LocalSearch3:

    def __init__(self, graph):
        self.SECONDS_TO_RUN = 60
        self.graph: Graph = graph
        self.colors: List[str] = self.graph.states[0].domain.initial_colors
        self.steps = 0
        self.steps_since_last_restart = 0
        self.restarts = 0
        self.queue = deque(maxlen=len(self.colors) + 1)

    # This function controls the overall algorithm. It performs the bulk of its work inside a while loop that runs
    # for up to 60 seconds. During every iteration of this loop, it picks a state with the most connected states of
    # the same color and assigns a new color to that state that produces the best value of the objective function:
    # min(connections between states with the same color in entire dataset). Then, if the objective function has a
    # value of 0 (0 connections between same-color states), it breaks and presents the results. If not, it adds
    # the state to a deque tracking the most recently changed n states where n = (number of colors to pick from + 1).
    # If only two unique states have been changed in the past n steps, this is an indication that the algorithm will
    # continually bounce between changing only these two, so it randomly reassigns every state and begins again.
    # Additionally, if 1000 steps have happened since the last random reassign, it randomly reassigns again as well.
    # If neither of these happen, it goes back to the top of the loop and picks the next most conflicted state.
    def search(self):
        self.randomAssign()
        self.restarts = 0
        t_start = time.time()
        completed = False

        # runs for 60 seconds
        while time.time() < t_start + self.SECONDS_TO_RUN:

            most_conflicted_state = self.findMostConflictedState()
            color_conflicts = self.fixConflictedState(most_conflicted_state)
            most_conflicted_state.color = color_conflicts
            self.incrementSteps()
            total_violations = self.calculateViolatedConstraints(self.graph)

            if total_violations == 0:
                completed = True
                break

            # Checks if the deque is full and only contains 2 unique states, or if 1000 steps have happened since
            # the last reassign
            if (len(set(self.queue)) <= 2 and len(self.queue) == self.queue.maxlen) or \
                    self.steps_since_last_restart % 1000 == 0:
                self.randomAssign()

            # appends the just-changed state to the deque
            self.queue.append(most_conflicted_state.name)

        if completed:
            print("States:\n" + self.graph.printStateColors())
            print("Local Search completed with " + str(self.calculateViolatedConstraints(self.graph)) +
                  " connected states of the same color.")
            print("Random reassigns after initial random assignment: " + str(self.restarts))
            print("Total steps: " + str(self.steps))
            print("Steps taken since last random reassign: " + str(self.steps_since_last_restart))
        else:
            print("Could not find optimal solution with local search in " + str(self.SECONDS_TO_RUN) +
                  " seconds after " + str(self.steps) + " steps and " + str(self.restarts) + " random reassigns")

    # Randomly picks from a list of colors that will result in the least possible conflicts
    def fixConflictedState(self, most_conflicted):
        # In the form { number_of_conflicts: [list of colors resulting in that many conflicts] }
        conflict_color_map = {}

        for c in most_conflicted.domain.initial_colors:
            new_graph = copy.deepcopy(self.graph)
            new_state = [x for x in new_graph.states if x.name == most_conflicted.name][0]
            new_state.color = c
            violated_constraints = self.calculateViolatedConstraints(new_graph)

            if violated_constraints in conflict_color_map.keys():
                conflict_color_map[violated_constraints] += [c]
            else:
                conflict_color_map[violated_constraints] = [c]

        # Identifies the lowest amount of conflicts possible, then randomly picks from one of the colors
        # producing that many conflicts
        least_conflicts = min(conflict_color_map.keys())
        chosen_color = random.choice(conflict_color_map[least_conflicts])

        return chosen_color

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

        # Identifies the highest amount of same-color connections out of all the states, then
        # randomly picks one of the states with that many conflicts
        most_conflicts = max(conflict_state_map.keys())
        chosen_state = random.choice(conflict_state_map[most_conflicts])

        return chosen_state

    def incrementSteps(self):
        self.steps += 1
        self.steps_since_last_restart += 1

    # Randomly assigns a color to every state
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
