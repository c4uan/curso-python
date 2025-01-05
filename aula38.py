"""
Repetições
While(enquanto) + continue
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

cont = 0

while cont <=100:
    cont += 1

    if cont == 6:
        print(f'Mariana não conta {cont}')
        continue

    print(f'Mariana conta {cont}')

    if cont == 40:
        break

print('Mariana contou tudo')