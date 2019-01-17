from math import sqrt


import math


class ComplexNumber:
    def __init__(self, re, im):
        self.a = re
        self.b = im
        if self.a == 0 and self.b == 0:
            print("Argument undefined")
            exit()

    def magnitude(self):
        return math.sqrt(self.a ** 2 + self.b ** 2)

    def argument(self):
        try:
            2 * math.atan(self.b / (math.sqrt(self.a ** 2 + self.b ** 2) + self.a))
        except ZeroDivisionError:
            return math.pi / 2
        else:
            return 2 * math.atan(self.b / (math.sqrt(self.a ** 2 + self.b ** 2) + self.a))