'''
Mariazinha sabe que um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo.
Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7 sem que
haja resto. Então ela pediu para você fazer um programa que aceite diversos valores e diga se cada um 
destes valores é primo ou não. Acontece que a paciência não é uma das virtudes de Mariazinha, portanto ela 
quer que a execução de todos os casos de teste que ela selecionar (instâncias) aconteçam no tempo
 máximo de um segundo, pois ela odeia esperar.
'''

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            print("Not prime")
            return False
        i += 6
    print("Prime")
    return True

n = int(input())
for _ in range(n):
    num = int(input())
    is_prime(num)