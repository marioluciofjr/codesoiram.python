# Instale a biblioteca num2words
!pip install num2words

# Importe o pacote necessário
from num2words import num2words

# Insira qual a tabuada que você quer. Ou seja, se você inserir o número 2, por exemplo, isso quer dizer que deseja a tabuada do 2. 
tabuada = int(input("Digite a tabuada: "))

# Insira a quantidade a ser multiplicada pela tabuada definida no passo anterior.
quantidade_max = int(input("Digite a quantidade máxima multiplicada: "))

# espaço no código.
print("\n")

# máximo de multiplicações.
range_max = tabuada * quantidade_max + 1

# contagem das linhas.
counter = 0

# estrutura de repetição para formar a tabuada.
for i in range(tabuada, range_max, tabuada):
    counter = counter + 1
    print(tabuada, "*", counter, "= ", i)
    num_ptbr = num2words(i, lang="pt-br")
    print(f"Resultado em Cardinal: {num_ptbr}")
    num_ptbr_ord = num2words(i, lang="pt-br", to="ordinal")
    print(f"Resultado em Ordinal: {num_ptbr_ord}\n")
