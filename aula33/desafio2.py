"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario_str = input('Que horas são? digite um número de 0 à 23. ')

try:
    horario_int = int(horario_str)

#Expressões lógicas para definir resposta do programa:
    bom_dia = horario_int >= 0 and horario_int <= 11
    boa_tarde = horario_int >= 12 and horario_int <=17
    boa_noite = horario_int >= 18 and horario_int <=23

    if bom_dia:
        print("Bom dia! :D")

    elif boa_tarde:
        print("Boa tarde! :D")

    elif boa_noite:
        print("Boa noite! :D")
    
    else:
        print("Horário maior ou menor que 0 e 23")

except:
    print('Digite um número inteiro.')