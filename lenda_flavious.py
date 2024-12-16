'''
Haverá NC (1 ≤ NC ≤ 30 ) casos de teste. Em cada caso de teste de entrada haverá um par de números inteiros
positivos n (1 ≤ n ≤ 10000 ) e k (1 ≤ k ≤ 1000). O  número n representa a quantidade de pessoas no círculo,
numeradas de 1 até n. O número k representa o tamanho do salto de um homem até o próximo homem que será
morto.
'''
teste = int(input())

def nova_lista_pessoas(lista, pulo):
    indice = 0  
    while len(lista) > 1:  
        indice = (indice + pulo) % len(lista)  
        lista.pop(indice)  
    return lista[0]  


for c in range(teste):
    pessoas, pulo = map(int, input().split())
    pulo = pulo - 1  
    lista_pessoas = [x for x in range(pessoas)]
    sobrevivente = nova_lista_pessoas(lista_pessoas, pulo)
    print(f"Case {c + 1}: {sobrevivente + 1}")

    

