a = 'A'
b = 'B'
c = 1.123456

formato = 'c = {:.2f} a = {} b = {}'.format(c, a, b)

string = 'a = {nome1} c = {nome3:.2f} b = {nome2}'
formato2 = string.format(
    nome1=a, nome2=b, nome3=c)

string2 = 'b = {1} a = {0} c = {2:.2f}'
formato3 = string2.format(a, b, c)

print(formato)
print(formato2)
print(formato3)