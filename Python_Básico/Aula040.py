# Calculadora com while

sair = ''
while True:
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    # sair = sair.lower() retorna string em minusculo
    # sair = sair.startswith('s') verifica se foi digitado "s" e retorna boolean
    print("saiu")
    