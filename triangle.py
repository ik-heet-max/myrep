from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            print("These segments won't make a triangle")
            exit(1)

    def area(self):
        half_perimeter = self.perimeter() / 2
        return sqrt(half_perimeter*(half_perimeter - self.a)*(half_perimeter - self.b)*(half_perimeter - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def sides(self):
        print("The segments of the triangle equal", self.a, ",", self.b, "and", self.c)