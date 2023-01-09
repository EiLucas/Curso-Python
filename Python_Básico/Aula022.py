# Operadores lógicos
# and(e) or(ou) not(não)

# our - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira. 
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '1234'
if (entrada == 'e' or entrada == 'E') and senha_digitada == senha_permitida:
     print('Entrou')
elif entrada == 's' or entrada == 'S':
    print('Saiu')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)