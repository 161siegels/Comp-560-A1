from typing import Dict, List
from Main.startup import checkArguments
from Main.fileReader import readFromFile
from Main.controller import Controller
from Models.Graph import Graph
from Models.LocalSearch import LocalSearch
from Models.BacktrackSearch import BacktrackSearch


file_name: str = checkArguments()
inputs: Dict[str, List[str]] = readFromFile(file_name)
c: Controller = Controller(inputs)


def main():
    runLocalSearch()
    runBacktrackingSearch()


def runLocalSearch():
    graph: Graph = c.organizeInput()
    local_search: LocalSearch = LocalSearch(graph, 123, file_name)
    local_search.localSearchController()


def runBacktrackingSearch():
    graph2: Graph = c.organizeInput()
    backtrack_search: BacktrackSearch = BacktrackSearch(graph2)
    print(backtrack_search)


if __name__ == '__main__':
    main()
