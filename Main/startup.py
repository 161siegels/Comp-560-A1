import sys
from os import path


def checkArguments() -> str:
    if len(sys.argv) != 2:
        print("Usage: python main.py [TEXT FILENAME]")
        print("For example: \"python main.py usa.txt\"")
        return ""
    else:
        if path.exists("Files/usa.txt"):
            print("Found file")
            return "Files/" + sys.argv[1]
        else:
            print("File not found, please make sure it was entered correctly.")
            return ""

