'''
carros = 'Corsa', 'Etios', 'Uno', 'Palio'
print(len(carros))
'''

carros = 'Corsa', 'Etios', 'Uno', 'Palio'
for veiculos in range(0, len(carros)):
    print(carros[veiculos])


for veiculos in carros:
    print(f'Veículo {veiculos}')
