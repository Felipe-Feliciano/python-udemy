"""
Interpolação báscias de strings
s - string
d e i - int
f - float
x e x - Hexadecimal (ABCDEF0123456789)

"""

nome = 'Felipe'
preco = 1450.678
variavel = '%s, o preço total foi R$%.2f' % (nome, preco) 
print(variavel)
print('O hexadecimal de %d é %08x' % (1500,1500))