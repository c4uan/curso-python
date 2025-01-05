# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 
#  C a u a n
# -5-4-3-2-1

nome = 'Cauan'
# print(nome[2])
# print(nome[-3])

# print('uan' in nome)
# print('Mag' in nome)
# print(10 * '-')
# print('Cau' not in nome)
# print('Sexo'not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} Está em {nome}')
else:
    print(f'{encontrar} Não está em {nome}')

