from typing import List


class Domain:

    def __init__(self, colors: List[str]):
        self.available_colors: List[str] = colors
        self.initial_colors: List[str] = colors

    def removeColor(self, color: str) -> bool:
        if color in self.available_colors:
            self.available_colors.remove(color)
            return True
        else:
            return False

    def resetColors(self):
        self.available_colors = self.initial_colors

    def addColor(self, color: str):
        self.available_colors.add(color)

    def __repr__(self):
        return "Colors remaining: " + str(self.available_colors)
