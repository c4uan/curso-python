# Title: Gerador de CPF
import random

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contr_1 = 10

    result_1 = 0
    for digit in nove_digitos:
        result_1 += int(digit) * contr_1
        contr_1 -= 1

    digito_1 = (result_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contr_2 = 11

    result_2 = 0
    for digit in dez_digitos:
        result_2 += int(digit) * contr_2
        contr_2 -= 1

    digito_2 = (result_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <=9 else 0

    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_gerado)