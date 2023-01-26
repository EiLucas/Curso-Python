# Repetições
# while(enquanto)
# break: finaliza o laço
# continue: volta para o ínicio do código.

qtd_linhas = 5
qtd_colunas = 5

linha = 1 #contador
while linha <= qtd_linhas:
    coluna = 1    
    while coluna < qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

qtd_linhas = 5
qtd_colunas = 5

linha = 1 #contador
while linha <= qtd_linhas:
    coluna = 1    
    while coluna < qtd_colunas:
        nome = input('Nome: ')
        print(f'{nome =}')
        coluna += 1
    linha += 1

print('FIM')