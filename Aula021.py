# Operadores lógicos
# and (e) or (ou) not (não)

# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '1234'
if entrada == 'e' and senha_digitada == senha_permitida:
    print('Entrou')
elif entrada == 's':
    print('Saiu')
