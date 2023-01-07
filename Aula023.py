# Operadores lógicos
# and(e) or(ou) not(não)

# Operador lógico "not" 
# Usado para inverter expressões
# not True = False
# not False = True 

senha = input('Senha: ') 

#if senha != '1234':
#    print('Senha errada!')

if not senha:
    print('Você não digitou nada')

print(not False) #True
print(not True)  #False
print(not 0)     #True
print(not 1)     #False