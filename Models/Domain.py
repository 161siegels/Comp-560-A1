from typing import List


class Domain:

    def __init__(self, colors: List[str]):
        self.available_colors: List[str] = colors
        self.initial_colors: List[str] = colors

    #Removes a color from the domain
    def removeColor(self, color: str) -> bool:
        if color in self.available_colors:
            self.available_colors = [x for x in self.available_colors if x != color]
            return True
        else:
            return False

    #Resets the domain to include all colors
    def resetColors(self):
        self.available_colors = self.initial_colors

    #Adds a color to the domain
    def addColor(self, color: str):
        self.available_colors += [color]

    def __repr__(self):
        return "Colors remaining: " + str(self.available_colors)
