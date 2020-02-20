import sys
from os import path, mkdir


def checkArguments() -> str:
    if not path.exists("Outputs"):
        mkdir("Outputs")
    if len(sys.argv) != 2:
        print("Usage: python main.py [TEXT FILENAME]")
        print("For example: \"python3 main.py usa.txt\"")
        exit(1)
    else:
        if path.exists("Files/" + sys.argv[1]):
            return "Files/" + sys.argv[1]
        else:
            print("File not found, please make sure it was entered correctly.")
            exit(1)

