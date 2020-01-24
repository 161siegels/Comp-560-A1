from Main.startup import checkArguments
from Main.fileReader import readFromFile
from Main.controller import Controller


def main():
    file_name = checkArguments()
    inputs = readFromFile(file_name)
    c = Controller(inputs)
    all_states = c.organizeInput()
    for s in all_states:
        print(s)


if __name__ == '__main__':
    main()
