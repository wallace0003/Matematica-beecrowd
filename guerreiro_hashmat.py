'''
Hashmat é um guerreiro cujo seu grupo de soldados se move de um local a outro para lutar contra os 
seus oponentes. Antes da luta ele apenas calcula uma coisa. A diferença entre a quantidade de soldados que possui e a
quantidade de soldados oponentes. A partir desta diferença ele decide se vai ou não lutar. Às vezes Hashmat tem mais soldados do
que o seu oponente, mas na maioria das vezes não.
'''

import sys

for line in sys.stdin:
    try:
        n1, n2 = map(int, line.split())
        print(abs(n1 - n2))
    except EOFError:
        break
