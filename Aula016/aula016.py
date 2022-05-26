'''
TUPLA -> Uma variável recebe mais de um valor.
    obs: TUPLAS SÃO IMUTÁVEIS, ou seja, uma vez atribuida um valor
         não é mais possível alterar, a não ser que mude o valor da 
         tupla.
'''

jogos = 'CS', 'GoW', 'RE8', 'Control'
print(jogos) # Mostra todos
print(jogos [0]) #  Mostra o CS
print(jogos [1]) #  Mostra o GoW
print(jogos [2]) #  Mostra o RE8
print(jogos [3]) #  Mostra o Control
print(jogos [0:]) #  Mostra todos os jogos
print(jogos [0::3]) #  Mostra o CS e Control
print(jogos [1:3]) #  Mostra GoW e RE8, porque no fatiamento, o elemento 3 é ignorado.
print(jogos [1:4]) #  Mostra  GoW, RE8 e Control
print(jogos [:2]) #  Mostra do CS, Gow (Ignora o elemento 2)

'''

 No caso de contagem negativa, a última variável é -1 e a primeira é -4.
 Por exemplo:
 
 jogos = 'CS', 'GoW', 'RE8', 'Control'
          -4    -3     -2       -1
 
-1 = Control    /   -2 = RE8    /   -3 = GoW    / -4 = CS
'''
print(jogos [:-2]) #  Mostra do CS, Gow (Ignora o elemento -2)
print(jogos [-2:]) #  Mostra do RE8 e Control
print(jogos [-3:]) #  Mostra do GoW, RE8 e Control
