#.count() mostra quantas vezes a palavra dentro do parenteses apareceu.
#.lower() deixa tudo em minusculo
#.upper() deixa tudo em maiusculo

frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido Van Rossum.'

print(frase)

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_vezes_letra_apareceu = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_vezes_letra_apareceu:
        qtd_apareceu_mais_vezes = qtd_vezes_letra_apareceu
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes}" que apareceu {qtd_apareceu_mais_vezes}')