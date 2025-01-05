nome = 'Cauan Magno'
altura = 1.78
peso = 96
imc = peso / altura ** 2

#f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'{nome} pesa {peso}Kg'
linha_3 = f'o IMC de {nome} é: {imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)