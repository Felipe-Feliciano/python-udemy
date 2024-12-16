# Operadores Lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São conseiderados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor


entrada = input('[E]ntra [S]air:')
senha_digitda = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitda == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem Senha'
print(senha)