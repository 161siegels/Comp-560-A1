from Main.startup import checkArguments
from Main.fileReader import readFromFile
from Main.controller import Controller
from Models.Graph import Graph


def main():
    file_name: str = checkArguments()
    inputs: str = readFromFile(file_name)
    print(inputs)
    c: Controller = Controller(inputs)
    graph: Graph = c.organizeInput()
    print(graph)


if __name__ == '__main__':
    main()
