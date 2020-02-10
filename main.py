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
    c2: Controller = Controller(inputs)
    graph: Graph = c.organizeInput()
    graph2: Graph = c2.organizeInput()
    runLocalSearch(graph)
    backtrack_search: BacktrackSearch = BacktrackSearch(graph2)
    print(backtrack_search)

def runLocalSearch(graph: Graph):
    local_search: LocalSearch = LocalSearch(graph, 123)
    local_search.localSearchController()

if __name__ == '__main__':
    main()
