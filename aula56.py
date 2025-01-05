"""
split e join com list e str
split - divide uma string. Retorna uma lista
join - une uma string
"""
frase = 'O rato    , roeu a roupa     ,    do rei de roma'
lista_frases_cruas = frase.split(',')

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)

frases_unidas = ''.join('abc')

print(frases_unidas)