#Manipulando chaves e valores em dicionários
pessoa = {}

##
##

#modo dinâmico de adicionar atributos ao dicionário
chave_nome = 'nome'
pessoa[chave_nome] = 'Cauan'

chave_sobrenome = 'sobrenome'
pessoa[chave_sobrenome] = 'Magno'

#outro modo para adicionar atributos ao dicionário
# pessoa['nome'] = 'Cauan'
# pessoa['sobrenome'] = 'Magno'

print(pessoa[chave_nome])

del pessoa[chave_sobrenome]

#sobe uma exceção que para o código e quebra o if.
# if pessoa['sobrenome']: 
#     print('Existe')

# 1ª forma solucionar erro das linhas 17 e 18:
# impedir que o código suba uma exceção
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# 2ª forma solucionar erro das linhas 17 e 18:
# tratar a exceção
try:
    if pessoa['sobrenome'] is not None:
        print(pessoa['sobrenome'])
except KeyError:
      print(f'a chave valor {chave_sobrenome} não existe ou foi deletada')

