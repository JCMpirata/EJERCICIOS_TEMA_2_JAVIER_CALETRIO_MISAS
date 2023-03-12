import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y == 0:
            return "Origen"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
    
    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Punto(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Punto(self.x * other.x, self.y * other.y)
    
    def __div__(self, other):
        return Punto(self.x / other.x, self.y / other.y)
    
    def vector(self, other):
        return Punto(other.x - self.x, other.y - self.y)
    
    def modulo(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def distancia(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
if __name__ == "__main__":
    p1 = Punto(2, 3)
    p2 = Punto(5, 5)
    print(p1)
    print(p1.cuadrante())
    print(p2)
    print(p2.cuadrante())
    print(p1.vector(p2))
    print(p1.modulo())
    print(p1.distancia(p2))
    print(p1 + p2)
    print(p1 - p2)
    print(p1 * p2)
    

    
    
    
