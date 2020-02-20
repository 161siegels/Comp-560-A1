from typing import Dict, List
from Main.startup import checkArguments
from Main.fileReader import readFromFile
from Main.controller import Controller
from Models.Graph import Graph
from Models.BacktrackSearch import BacktrackSearch
from Models.LocalSearch import LocalSearch

file_name: str = checkArguments()
inputs: Dict[str, List[str]] = readFromFile(file_name)
c: Controller = Controller(inputs)


def main():
    print("Running Local Search...")
    runLocalSearch3()
    print("\nRunning Backtracking Search...")
    runBacktrackingSearch()


def runLocalSearch3():
    graph: Graph = c.organizeInput()
    local_search3: LocalSearch = LocalSearch(graph)
    local_search3.search()


def runBacktrackingSearch():
    c2: Controller = Controller(inputs)
    graph2: Graph = c2.organizeInput()
    backtrack_search: BacktrackSearch = BacktrackSearch(graph2)
    print(backtrack_search)


if __name__ == '__main__':
    main()
