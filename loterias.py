# Importe o pacote Random
import random

# condicional para rodar o código até você finalizá-lo
menu_loterias = ""
while menu_loterias != 6:
    menu_loterias = int(input("""Escolha a loteria que deseja gerar os números aleatórios: 

1 - Mega-Sena
2 - Quina 
3 - Lotomania
4 - Lotofácil
5 - Todas as anteriores
6 - Finalizar o código

"""))

    # condicional de opções a partir do input do menu
    if menu_loterias == 1:
        mega_sena = random.sample(range(61), int(input("Digite um número de 6 a 15 para apostar na Mega-Sena: ")))
        print("Números para você jogar na Mega-Sena: ", mega_sena)
    elif menu_loterias == 2:
        quina = random.sample(range(81), int(input("Digite um número de 5 a 15 para apostar na Quina: ")))
        print("Números para você jogar na Quina: ", quina)
    elif menu_loterias == 3:
        lotomania = random.sample(range(101), 50)
        print("Números para você jogar na Lotomania: ", lotomania)
    elif menu_loterias == 4:
        lotofacil = random.sample(range(26), int(input("Digite um número de 15 a 18 para apostar na Lotofácil: ")))
        print("Números para você jogar na Lotofácil: ", lotofacil)
    elif menu_loterias == 5:
        mega_sena = random.sample(range(61), int(input("Digite um número de 6 a 15 para apostar na Mega-Sena: ")))
        print("Números para você jogar na Mega-Sena: ", mega_sena)
        print("\n")
        quina = random.sample(range(81), int(input("Digite um número de 5 a 15 para apostar na Quina: ")))
        print("Números para você jogar na Quina: ", quina)
        print("\n")
        lotomania = random.sample(range(101), 50)
        print("Números para você jogar na Lotomania: ", lotomania)
        print("\n")
        lotofacil = random.sample(range(26), int(input("Digite um número de 15 a 18 para apostar na Lotofácil: ")))
        print("Números para você jogar na Lotofácil: ", lotofacil)
    else:
        print("Script finalizado")
