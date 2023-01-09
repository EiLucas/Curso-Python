# Interpolação básica de strings
# s - string
# d e i - int
# f - float
# .<número de dígitos>f
# x e X - Hexadecimal (ABCDEF123456789)
# > - Esquerda 
# < - Direita
# ^ - Centro
# Sinal - + ou -
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >6}')
print(f'{variavel: <6}')
print(f'{variavel:-^9}')
print(f'{1000.123456789:.2f}')
print(f'{1000.123456789:+,.2f}')
print(f'{1000.123456789:-,.2f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')