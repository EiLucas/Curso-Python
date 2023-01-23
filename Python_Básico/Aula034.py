# Repetições
# while(enquanto)
# Execultar uma ação enquanto uma condição for verdadeira
# Loop infinito

condicao = True
while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Bem vindo {nome}.')

    if nome == 'sair':
        break

print('Flw')