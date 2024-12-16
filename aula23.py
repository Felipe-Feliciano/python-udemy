# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# F e l i p e
#-6-5-4-3-2-1


nome = 'felipe'
print(nome[3])
print(nome[-4])
print('i' in nome)
print('a' in nome)
print('fel' in nome)
print('fel' not in nome)
print('a' not in nome)

nome2 = input(' Digite seu nome: ')
encontrar = input(' Digite o que deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')