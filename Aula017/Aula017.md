'''

'''
# TUPLA: São imutáveis. Os valores não pode ser alterados.
lanche = 'pizza', 'suco', 'pastel', 'queijo'
print(lanche[1])


# LISTA: São mutáveis. Os valores podem ser alterados.
lanche = ['pizza', 'suco', 'pastel', 'queijo']
lanche[1] = 'Sprite' #  troca o valor "suco" por "Sprite"
lanche.append('uva') #  o valor "uva" foi incluído a lista "lanche"
lanche.insert(0, 'cereal') #  Insere o valor "cereal" na posição 0 da lista "lanche"
del lanche[0] #  Remove o valor "pizza" da lista "lanche".
lanche.pop(0) #  Remove o valor "pizza" da lista "lanche".
lanche.remove('pizza') #  Remove o valor "pizza" da lista "lanche".
print(lanche[1]) #  Imprime o valor "suco"
print(lanche[4]) #  Imprime o valor "uva" adicionado pelo comando "append".

# COMO REMOVER O VALOR "PIZZA" SE ESTIVER NA LISTA LANCHE:

if 'pizza' in lanche:
    lanche.remove('pizza')

# Decalrando uma lista com  camando "range":

valores = list(range(4, 11)) # Cria uma lista com o nome "valores" do 4 ao 10.

valores = [5, 7, 8, 2, 1, 0, 9] # Cria uma lista com os valores informados dentro dos colchetes.
    print(len(valores)) # Conta quantos caracteres tem na variável "valores".
valores.sort() # Irá organizar os números em ordem crescente
valores.sorte(reverse = True) # Irá organizar os números em ordem decrescente
