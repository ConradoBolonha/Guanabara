'''
galera = [['Alan, 54], ['Elisa', 26], ['Pedro', 15], ['Beatriz', 41]]
print(galera[2][1])
'''

galera = [['Alan', 54], ['Elisa', 26], ['Pedro', 15], ['Beatriz', 41]]
for pessoal in galera:
    #  print(pessoal[0], end=', ')
    print(f'{pessoal[0]} tem {pessoal[1]} anos de idade.')
     