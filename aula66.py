"""
Esta função demonstra o conceito de argumentos posicionais (não nomeados) e argumentos nomeados em Python.

Argumentos posicionais:
- Estes são argumentos que precisam ser incluídos na posição ou ordem correta.
- Por exemplo, na chamada da função `func(10, 20)`, `10` e `20` são argumentos posicionais.

Argumentos nomeados:
- Estes são argumentos que são passados para a função especificando explicitamente o nome do parâmetro.
- Por exemplo, na chamada da função `func(a=10, b=20)`, `a` e `b` são argumentos nomeados.
- Argumentos nomeados podem ser fornecidos em qualquer ordem, e eles tornam a chamada da função mais legível.

A função abaixo aceita tanto argumentos posicionais quanto argumentos nomeados, demonstrando como eles podem ser usados juntos.
"""


def soma(x , y , z):
    #Definição da função soma
    print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)


print(soma) # Mostra a posição de memória da função soma
print(soma(10, 20, 30)) # Mostra o resultado da função soma e retorna None

soma(10, 20, 30) # Argumentos posicionais
soma(x=10, y=20, z=30) # Argumentos nomeados
