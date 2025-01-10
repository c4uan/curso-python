"""
Higher Order Functions
Funções de primeira classe
"""

# Função que recebe uma mensagem e um nome, e retorna uma saudação formatada
def meetings(msg, nome):
    return f'{msg}, {nome}!'

# Função de ordem superior que recebe outra função e seus argumentos, e executa a função passada com os argumentos fornecidos
def execute(function, *args):
    return function(*args)

# Chamando a função execute, passando a função meetings e seus argumentos
print(
    execute(meetings, 'Bom dia', 'Cauan')
)

# Chamando a função execute novamente com diferentes argumentos
print(
    execute(meetings, 'Boa noite', 'Flávia')
)