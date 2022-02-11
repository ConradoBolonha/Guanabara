
# FAÇA UM ALGORITMO QUE ANALISE O VALOR DIGITADO.

print('### Analisando valores digitados ### \n')
algo = input('Digite algo: ')
print('O tipo primitivo do valor é:', type(algo))
print('Tem espaços? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético? ', algo.isalpha())
print('É alfanumérico? ', algo.isalnum())
print('Está em maiúscula? ', algo.isupper())
print('Está em minúscula? ', algo.islower())
print('Está capitalizado? ', algo.istitle())
print(' ### FIM ###')
