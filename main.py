from Main.startup import checkArguments
from Main.fileReader import readFromFile
from Main.controller import Controller
from Models.Graph import Graph
from Models.LocalSearch import LocalSearch
from Models.BacktrackSearch import BacktrackSearch


def main():
    file_name: str = checkArguments()
    inputs: str = readFromFile(file_name)
    print(inputs)
    c: Controller = Controller(inputs)
    runLocalSearch(inputs, c)
    runBacktrackingSearch(inputs, c)


def runLocalSearch(inputs: str, c: Controller):
    graph: Graph = c.organizeInput()
    local_search: LocalSearch = LocalSearch(graph, 123)
    local_search.localSearchController()


def runBacktrackingSearch(inputs: str, c2: Controller):
    graph2: Graph = c2.organizeInput()
    backtrack_search: BacktrackSearch = BacktrackSearch(graph2)
    print(backtrack_search)


if __name__ == '__main__':
    main()
