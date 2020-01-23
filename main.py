from Main.startup import checkArguments
from Main.fileReader import readFromFile


def main():
    file_name = checkArguments()
    inputs = readFromFile(file_name)
    print(inputs)


if __name__ == '__main__':
    main()
