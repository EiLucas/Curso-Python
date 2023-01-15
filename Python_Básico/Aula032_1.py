"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um numero inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    if par_impar:
        print(f'O numero {numero} é par.')
    else:
        print(f'O numero {numero} é impar.')
else:
    print(f'{numero} não é um numero inteiro.')

#Ou

try:
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    if par_impar:
        print(f'O numero {numero} é par.')
    else:
        print(f'O numero {numero} é impar.')
except:
    print(f'{numero} não é um numero inteiro.')