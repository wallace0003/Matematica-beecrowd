'''
No planeta Alpha vive a criatura Blobs, que come precisamente 1/2 de seu suprimento de comida
 disponível todos os dias. Escreva um algoritmo que leia a capacidade inicial de suprimento 
 de comida (em Kg), e calcule quantos dias passarão antes que Blobs coma todo esse suprimento 
 até restar um quilo ou menos.
'''

n = int(input())

for _ in range(n):
    co = float(input())
    dias = 0

    while co > 1:
        co /= 2
        dias += 1
    print(f"{dias} dias")

