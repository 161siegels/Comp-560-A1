class OutputWriter:

    # pass in the same file_name as is in main.py along with a method which
    # is either "localsearch" or "backtracking"
    def __init__(self, file_name: str, method: str):
        self.method: str = method
        self.file_name: str = self.convertFilenameToOutput(file_name)

    # Writes the file with the new name into the Outputs/ folder that is created on startup
    def writeToOutput(self, output: str):
        file = open(self.file_name, "w+")
        file.write(output)

    # Converts file like Files/usa2.txt to Outputs/usa2_localsearch.txt
    def convertFilenameToOutput(self, file_name) -> str:
        return "Outputs/" + file_name.split("/")[1].split(".")[0] + "_" + self.method + ".txt"
