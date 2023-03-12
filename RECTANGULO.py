import PUNTO as pt
import math

class Rectangulo:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def base(self):
        return abs(self.p1.x - self.p2.x)
    
    def altura(self):
        return abs(self.p1.y - self.p2.y)

    def area(self):
        return abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y)

    def perimetro(self):
        return 2 * (abs(self.p1.x - self.p2.x) + abs(self.p1.y - self.p2.y))

    def diagonal(self):
        return math.sqrt((self.p1.x - self.p2.x)**2 + (self.p1.y - self.p2.y)**2)

    def __str__(self):
        return "Rectangulo con esquinas en los puntos ({}, {}) y ({}, {})".format(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
    
