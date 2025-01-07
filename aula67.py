"""
Valores padrão para parâmetros
ao definir uma função, os parâmetros podem ter vários valores padrão
caso o valor não seja enviado para o parâmetro, o valor padrão será utilizado

Refatorar: editar seu código.
"""

def soma(x ,y, z=None):
    if z is not None:
        print(f'{x=} + {y=} + {z=} ', '|', f'{x} + {y} + {z} =', x + y + z)
    else:
        print(f'x={x} + y={y} =', x + y)


soma(10, 20)
soma(10, 30)
soma(10, 40, 50)