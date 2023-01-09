# Introdução ao try/except
# try -> tentar executar o código
# except -> ocorreu algum erro ao tentar execultar

numero_str = input('Vou dobrar o número que você digitar: ')

try :
   print(f'String:{numero_str}', type(numero_str))# Mostra que o número digitado é uma string
   numero_float = float(numero_str)# Convert str para float
   print(f'Float:{numero_float}', type(numero_float))# Mostra o número convertido
   print(f'O dobro de {numero_str} é {numero_float * 2}')# Dobra o valor digitado
except:
    print('Isso não é um número')

#if numero_str.isdigit():
#    numero_float = float(numero_str)
#    print(f'O dobro de {numero_str} é {numero_float * 2}')
#else:
#    print('Isso não é um número')