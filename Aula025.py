# Interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF123456789)

nome = 'Lucas'
preco = 1000.9876543
variavel = '%s, o preço total é R$%f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (1505 , 1505)) #1505 é 05e1