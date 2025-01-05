"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


numero_str = input('Digite um número inteiro: ')


try:

    numero_int = int(numero_str) #Converte a entrada de String para Inteiro

    modulo = numero_int % 2 == 0 #Expressão para verificar se o número é par ou ímpar

    if modulo :
        print(f'O Número {numero_str} é par.') 
    else:
        print(f'O Número {numero_str} é ímpar')

except:
    print('Você não digitou um número inteiro')