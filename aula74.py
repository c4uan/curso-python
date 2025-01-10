"""
Closure e funções que retornam outras funções
"""

def create_greetings(greetings):
    def meet(name):
        return f'{greetings}, {name}!'
    return meet

greet_gmorning = create_greetings('Bom dia')
greet_gnight = create_greetings('Boa noite')

for name in ['Maria', 'Joana', 'Cauan']:
    print(greet_gnight(name))
    print(greet_gmorning(name))