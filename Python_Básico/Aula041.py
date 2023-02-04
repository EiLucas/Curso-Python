# while/else
# else sempre vai ser execultado, a não ser que haja um break

string = 'valor qualquer'
i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')