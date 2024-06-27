'''Leia dois valores inteiros M e N indefinidamente. A cada leitura, calcule e escreva a soma 
dos fatoriais de cada um dos valores lidos. Utilize uma variável apropriada, pois cálculo pode
 resultar em um valor com mais de 15 dígitos.'''



import sys

def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        return False
    else:
        fatoracao = 1
        for c in range(1, num + 1):
            fatoracao *= c
        return fatoracao

input = sys.stdin.read
data = input().split()

i = 0
while i < len(data):
    num1, num2 = int(data[i]), int(data[i+1])
    num1, num2 = factorial(num1), factorial(num2)
    print(num1 + num2)
    i += 2
