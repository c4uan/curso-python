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

multiplicacao = multiplicar(1, 2, 3, 4, 5 ,6)
print(multiplicacao)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def paircheck(numero):#recebe o parâmetro da variável que utiliza a função
    pair = numero % 2 == 0

    if pair:
        return f'{numero} é par'
    else:
        return f'{numero} é ímpar'

is2pair = paircheck(2)
print(is2pair)
print(paircheck(3))
print(paircheck(5))
print(paircheck(6))
print(paircheck(98762))
