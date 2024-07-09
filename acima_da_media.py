'''
Sabe-se que 90% dos calouros tem sempre a expectativa de serem acima da média no início de suas
graduações. Você deve checar a realidade para ver se isso procede.
'''

import sys

n = int(input())


for _ in range(n):
    input = sys.stdin.read()
    entrada = input.split()
    lista = list(map(int , entrada[1:]))
    media = sum(lista) / len(lista)
    acima = 0

    for nota in lista:
        if nota > media:
            acima += 1

    porcentagem = float((acima / len(lista)) * 100)
    porcentagem = round(porcentagem , 3)
    print(f"{porcentagem:.3f}")
    

