from typing import Dict

from Main.startup import checkArguments
from Main.fileReader import readFromFile
from Main.controller import Controller


def main():
    file_name = checkArguments()
    inputs: str = readFromFile(file_name)
    print(inputs)
    c = Controller(inputs)
    all_states = c.organizeInput()
    for s in all_states["states"]:
        print(s)
    for k in all_states["edges"].keys():
        print(k + ":")
        print(all_states["edges"][k])


if __name__ == '__main__':
    main()
