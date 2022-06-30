'''
Crie um programa onde o usuário digite uma expressão qualquer que use parêntese. Seu
aplicativo deverá analisar se a expressão está com os parênteses abertos
e fechados na ordem correta.
'''

expressao = str(input('Digite a expressão: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')
