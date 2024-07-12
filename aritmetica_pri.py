'''
As crianças são ensinadas a adicionar vários dígitos da direita para a esquerda, um dígito de cada vez. Muitos 
acham a operação "vai 1" (em inglês chamada de "carry", na qual o valor 1 é carregado de uma posição para ser 
adicionado ao dígito seguinte) um desafio significativo. Seu trabalho é para contar o número de operações de c
arry para cada um dos problemas de adição apresentados para que os educadores possam avaliar a sua 
dificuldade.
'''

def vai_1(n, n2):
    carry = 0
    mais_1 = 0
    len_n, len_n2 = len(n), len(n2)
    max_len = max(len_n, len_n2)
    
    
    n = n.zfill(max_len)
    n2 = n2.zfill(max_len)
    
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(n[i]) + int(n2[i]) + carry
        if digit_sum >= 10:
            carry = 1
            mais_1 += 1
        else:
            carry = 0

    if mais_1 == 1:
        print("1 carry operation.")
    elif mais_1 > 1:
        print(f"{mais_1} carry operations.")
    else:
        print("No carry operation.")

while True:
    n, n2 = input().split()
    if n == '0' and n2 == '0':
        break
    else:
        vai_1(n, n2)