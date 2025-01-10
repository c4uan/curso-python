# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def create_multiplier(factor):
    def multiplier(numeral):
        return numeral * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)
tenfold = create_multiplier(10)
fortyfold = create_multiplier(40)

v1= double(10)
v2= triple(10)
v3= quadruple(10)
v4= tenfold(10)
v5= fortyfold(10)

print(v1, v2, v3, v4, v5)
