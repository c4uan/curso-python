"""
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

#Lembrete de desempacotamento

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):#recebe e empacota os argumentos
    total = 0
    for numero in args:
        total +=  numero
    return total

numeros = (1, 2, 3, 4, 5, 6)
soma_1 = soma(*numeros)#desempacota os argumentos e envia como parâmetros
                       #para a função
print(soma_1)

print(sum(numeros)) #Função sum() do Python
