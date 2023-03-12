import PUNTO as pt
import RECTANGULO as rec
import math

if __name__ == "__main__":
    A = pt.Punto(2, 3)
    print(A)
    print(A.cuadrante())
    B = pt.Punto(5, 5)
    print(B)
    print(B.cuadrante())
    C = pt.Punto(-3, -1)
    print(C)
    print(C.cuadrante())
    D = pt.Punto(0, 0)
    print(D)
    print(D.cuadrante())

    print("Vector AB: ", A.vector(B))
    print("Vector BA: ", B.vector(A))

    print("Modulo de A: ", A.modulo())
    print("Modulo de B: ", B.modulo())

    print("Distancia entre A y B: ", A.distancia(B))
    print("Distancia entre B y A: ", B.distancia(A))

    r = rec.Rectangulo(A, B)
    print(r)
    print("Base: ", r.base())
    print("Altura: ", r.altura())
    print("Area: ", r.area())
    print("Perimetro: ", r.perimetro())
    print("Diagonal: ", r.diagonal())