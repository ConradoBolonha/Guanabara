"""
Colorindo o terminal

      ***  STYLE  ***           ***  TEXT  ***              ***  BACK GROUND  ***
0 - None                        30 - Branco                 40 - Branco
1 - Bold (negrito)              31 - Vermelho               41 - Vermelho
4 - Underline (Sublinhado)      32 - Verde                  42 - Verde
7 - Negative (Inverte a cor)    33 - Amarelo                43 - Amarelo
                                34 - Azul escuro            44 - Azul Claro
                                35 - Roxo                   45 - Roxo
                                36 - Azul claro             46 - Azul claro
                                37 - Cinza                  47 - Cinza

"""                 
print('\033[31mOlá Mundo!')             # Olá mundo em vermelho.
print('\033[31;44mOlá Mundo!\033[m')    # Olá mundo com texto vermelho, fundo azul claro só onde tem texto.
print('\033[1;32;43mOlá Mundo!')        # Olá mundo com texto estilo negrito, texto verde e fundo amarelo.
print('\033[4;30;45mOlá Mundo!\033[m')  # Olá mundo sublinhado, texto branco e fundo roxo.
print('\033[7;33;44mOlá Mundo!\033[m')  # 

a = 2
b = 6
s = a + b
print('A soma de \033[31m{}\033[m e \033[32m{}\033[m é \033[34m{}\033[m'.format(a, b, s))
nome = 'Conrado'
print('\nOlá, muito prazer em te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))
