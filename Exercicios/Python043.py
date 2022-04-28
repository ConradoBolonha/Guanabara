"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
seu IMC e mostre seu status de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso.
- Entre 18.6 e 24.9: Peso ideal.
- 25 até 29.9: Sobrepeso.
- 30 até 39.9: Obesidade
- Acima de 40: Obesidade mórbida
"""

print('\n ### CALCULE SEU IMC ###')
altura = float(input('\nDigite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('Seu IMC é {:.2f}. Você está abaixo do peso ideal.'.format(imc))
elif imc >= 18.6 and imc <= 24.9:
    print('Seu IMC é {:.2f}. Você está no peso ideal.'.format(imc))
elif imc >= 25 and imc <= 29.9:
    print('Seu IMC é {:.2f}. Você está com sobrepeso.'.format(imc))
elif imc >= 30 and imc <= 39.9:
    print('Seu IMC é {:.2f}. Você está obeso.'.format(imc))
elif imc >= 40:
    print('Seu IMC é {:.2f}. Você está com obesidade mórbida.'.format(imc))
