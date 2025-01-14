# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

# pessoa = dict(nome= 'Cauan', sobrenome= 'Magno')

#Forma mais comum de criar dicionários
pessoa = {
    'nome': 'Cauan',
    'sobrenome': 'Magno',
    'idade': 21,
    'altura': 1.78,
    'endereços':[
        {'rua': 'Tal tal', 'numero': 123},
        {'rua': 'isso aquilo', 'numero': 321},
    ]
    ,
}

# Acessando atributos manualmente
print(pessoa['nome'])
print(pessoa['sobrenome'])
print()

"""
for para iterar atributos
dict não é um tipo de dado iterável
mas o for utiliza automaticamente
o método dict.values() da classe dict 
para realizar a iteração
sobre os valores
"""

for chave in pessoa:
    print(chave, pessoa[chave])
