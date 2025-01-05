"""
Repetições
While(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True

while True:
    nome = input('Qual seu nome?')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        condicao == False
        break

print('Acabou')