import os 

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite um numero int.')
        except IndexError:
            print('Indice não existe na lista.')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':
        
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    
    elif opcao == 's':
        break
        
    else:
        print('Escolha i, a, l ou s')