# Fatiamento de strings
# 012345678
# Olá mundo
#-987654321
# Fatiamento [i:f:p] [::]
# Obs.: a função len retorna a qtd
# de caracteres da str

variavel = 'Olá mundo'
print(variavel[4:9])
print(variavel[-9:])
print(variavel[:-1])
print(variavel[::-1])
print(len(variavel[:-1]))
print(len(variavel))# Retorna o tamanho da string
print(variavel[0:len(variavel):1])
print(variavel[0:9:4])
print(variavel[-1:-10:-1])
print(variavel[-1:-10:-3])