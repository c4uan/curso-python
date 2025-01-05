"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_str = input("Digite seu nome: ")

if nome_str:
    tamanho_nome = len(nome_str)

#Expressões organizadas para entender melhor as condições das linhas 19 - 26
    nome_pequeno = tamanho_nome <= 4

    nome_normal = tamanho_nome == 5 and tamanho_nome <= 6

    nome_grande = tamanho_nome >=6

    if nome_pequeno:
        print(f"Seu nome tem {tamanho_nome} letras, seu nome é curto")
        
    if nome_normal:
        print(f"Seu nome tem {tamanho_nome} letras, seu nome é normal")

    if nome_grande:
        print(f"Seu nome tem {tamanho_nome} letras, seu nome é grande")

else:
    print("Digite um nome")