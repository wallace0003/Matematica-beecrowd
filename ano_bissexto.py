def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
    
def huluku(ano):
    if ano % 15 == 0:
        return True
    else:
        return False

def bulucuku(ano):
    if ano % 55 == 0:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            return True
        else:
            return False
    else:
        return False

while True:
    try:
        ano = int(input())
        if bissexto(ano):
            print("This is leap year.")
        if huluku(ano):
            print("This is huluculu festival year.")
        if bulucuku(ano):
            print("This is buluculu festival year.")
        if not bissexto(ano) and not huluku(ano) and not bulucuku(ano):
            print("This is an ordinary year")
            
        

    except EOFError:
        break