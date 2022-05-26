lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita'

for comida in lanche:
    print(f'Eu vou comer {comida}')

for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador}')

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')

print(sorted(lanche)) # Coloca as variáveis em ordem alfabética.