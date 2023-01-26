# Repetições
# while(enquanto)
# break: finaliza o laço
# continue: volta para o ínicio do código.


contador = 0

while contador <= 1000:
    contador += 1

    if contador == 6:
        print('Não mostra o 6')
        continue

    if contador >=10 and contador <=27:
        print(f'Não mostra o {contador}')
        continue

    print(contador)

    if contador == 40:
        break

print('FIM')