"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

"""
Métodos úteis:
    append - Adiciona um item ao final da lista
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
    Create Read Update Delete - CRUD
"""
lista_a = [1, 2 ,3]
lista_b = [4, 5 ,6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)

print(lista_a)
print(lista_c)
print(lista_d)
# print(lista[3])
# del lista[2]
# print(lista[2])
# lista.append('Sirius')
# lista.pop()
# lista.append(80)
# lista.append(0)
# ultimo_valor = lista.pop(1)
# # lista.clear()
# lista.insert(0, 2)
# print(lista, 'Removido', ultimo_valor)

