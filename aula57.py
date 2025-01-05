"""
Listas de listas e seus índices
"""

salas = [
    # 0       1
    ['Ana', 'Carlos'], # 0
    # 0
    ['Pedro',], # 1
    # 0         1        2
    ['Helena', 'Jonas', 'Alice',], # 2
    # 0       1       2
    ['José', 'Jorge', 'Júlia',], # 3
]

# print(salas[1][0]) # Pedro
# print(salas[0][1]) # Carlos
# print(salas[2][2]) # Alice
# print(salas[2][3][2]) # 20

for sala in salas:
    print(f'a sala é: {sala}')
    for aluno in sala:
        print(aluno)
        