"""'
Crie um programa que lei o nome de uma cidade e diga
se ela começa ou não com o nome "Santo"
"""

cidade = input('Digite o nome composto de uma cidade: ')
div_cid = cidade.split()
print ('Santo' in div_cid[0])
