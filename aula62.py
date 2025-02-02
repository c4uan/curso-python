
#CPF - 73446348050

entrada_cpf = '73446348050'
nove_digitos = entrada_cpf[:9]
contr_1 = 10


resultado_digito_1 = 0
for digit in nove_digitos:
    resultado_digito_1 += int(digit) * contr_1
    contr_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contr_2 = 11

resultado_digito_2 = 0
for digit in dez_digitos:
    resultado_digito_2 += int(digit) * contr_2
    contr_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <=9 else 0

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_gerado == entrada_cpf:
    print('CPF válido')
else:
    print('CPF inválido')