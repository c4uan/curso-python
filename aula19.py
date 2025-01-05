primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

primeira_entrada = float(primeiro_valor)
segunda_entrada = float(segundo_valor)

if primeira_entrada > segunda_entrada:
    print(f'O primeiro valor: {primeira_entrada} \né maior que o segundo: {segunda_entrada}')

elif segunda_entrada > primeira_entrada:
    print(f'O segundo valor: {segunda_entrada} \né maior que o primeiro: {primeira_entrada}')
