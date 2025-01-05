a = 'A'
b = 'B'
c = 1.1
string ='a = {nome1} \nb = {nome2}\nc = {nome3:.2f}'

formato = string.format(
    nome1 = a,
    nome2 = b,
    nome3 = c
    ) 

print(formato)

#ou Seja

nome = 'Cauan Magno'
peso = 90
altura = 1.78
imc = peso / altura ** 2
string = 'O {saida1} pesa {saida2} e tem {saida3} de altura, o IMC de {saida1} é: {saida4:.2f}'
formato = string.format(
    saida1 = nome,
    saida2 = peso,
    saida3 = altura,
    saida4 = imc
    )

print(formato)
