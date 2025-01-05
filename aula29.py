# introdução ao try/except
# try -> tentar executar o código
# except -> ocorreu algum erro ao tentar executar

numero_str = input(
    'Vou dobrar o que vc digitar: '
    )

try:

    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float*2:.2f} ')

except:

    print('Isso não é um número')