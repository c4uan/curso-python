# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1, 2, 3, 4, 5, 6)
print(multiplicacao)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):

    multiplode2 = numero % 2 == 0

    if multiplode2:
        return f'{numero} é par'
    else:
        return f'{numero} é impar'

outro_par_impar = par_impar(10)
dois_par_impar = par_impar(2)
print(dois_par_impar)
print(par_impar(3))
print(par_impar(4))