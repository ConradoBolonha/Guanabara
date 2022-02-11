
# Escreva um programa que leia em metros e o exiba convertido em centímetros e milímetros.

num = float(input('Digite um número em metros: '))
num_km = (num*0.001)
num_hm = (num*0.01)
num_dam = (num*0.1)
num_dm = (num*10)
num_cm = (num*100)
num_mm = (num*1000)
print('O número {} corresponde a {} quilômetros'.format(num, num_km))
print('O número {} corresponde a {} hectômetros'.format(num, num_hm))
print('O número {} corresponde a {:.2f} decâmetros'.format(num, num_dam))
print('O número {} corresponde a {} decímetros'.format(num, num_dm))
print('O número {} corresponde a {} centímetros'.format(num, num_cm))
print('O número {} corresponde a {} milímetros'.format(num, num_mm))
