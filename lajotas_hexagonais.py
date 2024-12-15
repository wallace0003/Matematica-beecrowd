dici = {
    "left" : [x for x in range(1,40,2)], #Contém só número ímpares
    "right" : [y for y in range(2,41, 2)]# contém só número pares
}

#parada tem que ser no dest
#faça todos as rotas - as rotas que voltam um passo para trás.
def n_rotas(dest):

    atual = 0

    if dest in dici["left"]:
        atual = dici["left"][0]
        print(atual)
        

    elif dest in dici["right"]:
        ...

    
    


while True:
    dest = int(input())

    if dest == 0: 
        break

    elif dest > 0:
        n_rotas(dest)

