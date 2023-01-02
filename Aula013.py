nome = 'Lucas'
altura = 1.90
peso = 115
imc = peso / altura ** 2

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é {imc:.2f}'

print(linha_1)
print(linha_2)