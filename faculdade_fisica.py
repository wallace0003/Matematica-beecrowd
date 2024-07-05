'''
Uma partícula tem velocidade inicial e aceleração constante. Se a sua velocidade após certo
 momento é v então qual será seu deslocamento no dobro deste tempo?
'''

import sys

def main():
    interacao = sys.stdin.read()
    data = interacao.split()
    
    i = 0
    results = []
    while i < len(data):
        v = int(data[i])
        t = int(data[i+1])
        i += 2
        s = 2 * v * t
        results.append(s)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
