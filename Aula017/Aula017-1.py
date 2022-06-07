numero = [1, 9, 3, 8, 0, 5]
numero[1] = 7 # Muda o valor 9 para 7.
numero.append(6) # Adiciona o valor 6 a lista "numero"
numero.sort(reverse=True)
numero.insert(2, 11) # Adiona o valor 11 na posição 2.
numero.pop(2) # Elimina o valor 11 da lista.
print(numero)
print(f'Essa liste tem {(len(numero))} elementos.')
