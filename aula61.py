
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
