'''
Paulinho tem em suas mãos um pequeno problema. A professora lhe pediu que ele construísse um programa para
verificar, à partir de dois valores inteiros A e B, se B corresponde aos últimos dígitos de A.
'''


n  = int(input())

for _ in range(n):
    n, n2 = str(input()).split()

    come_n = len(n) - len(n2)

    if n[come_n:] == n2:
        print("encaixa")
    else:
        print("nao encaixa")
