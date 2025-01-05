"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor  por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

text = ('Luiz') # iterável

iterator = iter(text) # iterador

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

print(''.zfill(10))

for letra in text:
    print(letra)


