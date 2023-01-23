# http://docs.pythom.org/pt-br/3/library/stdtypes.html
# Imutáveis que vimos: str, int, float, bool

string = 'lucas alves'
outra_variavel = f'{string[:3]}asa{string[5:]}'

print(outra_variavel)
print(string)
print(string.capitalize())# Primeira letra maiuscula
print(string.zfill(1000))