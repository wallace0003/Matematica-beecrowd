'''Em uma terra distante existem duas cidades, a Nlogônia onde vivem os Nlogoneses, e 
Ducklogônia onde vivem seus vizinhos os Duckneses, já à algum tempo estas duas cidades estão 
em guerra e agora em uma tentativa de ganhar a guerra os Duckneses pretendem atacar a cidade 
da Nlogônia com um bodoque que atira patos, porem para que não haja erro eles pediram que você 
construa um programa que dados os valores da altura do bodoque (h), os pontos onde inicia (p1) 
e onde termina (p2) a cidade da Nlogônia, o ângulo do disparo (a) e a velocidade do 
lançamento, calcule se o projetil atingira o alvo.'''



import sys
from math import sin, cos, radians, sqrt

G = 9.80665

def distancia_maxima(vo, angulo, G, h):
    angulo_rad = radians(angulo)
    parte1 = (vo * cos(angulo_rad)) / G
    parte2 = (vo * sin(angulo_rad)) + sqrt((vo * sin(angulo_rad))**2 + 2 * G * h)
    alcance = parte1 * parte2
    return round(alcance, 5)

def main():
    input = sys.stdin.read
    data = input().split()
    i = 0

    while i < len(data):
        h = float(data[i])
        i += 1

        pi, pf = int(data[i]), int(data[i + 1])
        i += 2

        tentativas = int(data[i])
        i += 1

        for _ in range(tentativas):
            angulo, vo = float(data[i]), float(data[i + 1])
            i += 2
            alcance = distancia_maxima(vo, angulo, G, h)

            if pi <= alcance <= pf:
                print(f"{alcance:.5f} -> DUCK")
            else:
                print(f"{alcance:.5f} -> NUCK")

if __name__ == "__main__":
    main()
