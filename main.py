from typing import Dict, List
from Main.startup import checkArguments
from Main.fileReader import readFromFile
from Main.controller import Controller
from Models.Graph import Graph
from Models.LocalSearch import LocalSearch
from Models.BacktrackSearch import BacktrackSearch
from Models.LocalSearch2 import LocalSearch2

file_name: str = checkArguments()
inputs: Dict[str, List[str]] = readFromFile(file_name)
c: Controller = Controller(inputs)


def main():
    runLocalSearch2()
    # runLocalSearch()
    runBacktrackingSearch()


def runLocalSearch2():
    graph: Graph = c.organizeInput()
    local_search2: LocalSearch2 = LocalSearch2(graph)
    local_search2.search()


def runLocalSearch():
    graph: Graph = c.organizeInput()
    local_search: LocalSearch = LocalSearch(graph, 123, file_name)
    local_search.localSearchController()


def runBacktrackingSearch():
    c2: Controller = Controller(inputs)
    graph2: Graph = c2.organizeInput()
    backtrack_search: BacktrackSearch = BacktrackSearch(graph2)
    print(backtrack_search)


if __name__ == '__main__':
    main()
