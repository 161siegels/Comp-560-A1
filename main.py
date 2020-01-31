from Main.startup import checkArguments
from Main.fileReader import readFromFile
from Main.controller import Controller
from Models.Graph import Graph
from Models.LocalSearch import LocalSearch


def main():
    file_name: str = checkArguments()
    inputs: str = readFromFile(file_name)
    print(inputs)
    c: Controller = Controller(inputs)
    graph: Graph = c.organizeInput()
    local_search: LocalSearch = LocalSearch(graph)
    print(local_search)


if __name__ == '__main__':
    main()
