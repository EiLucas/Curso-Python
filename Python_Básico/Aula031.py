# Flag (Bandeira) - Marca um local
# None = não valor
# is e is not = é ou não é (tipo, valor, identidade)
# id = identidade

v1 = 'a' 
v2 = 'a' # mesmo endereço de memória, por terem o mesmo valor.

print(id(v1)) 
print(id(v2)) 

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
    
#if passou_no_if is not None:
#    print('Passou no if')    