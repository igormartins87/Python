palavra = input("Digite uma palavra:")

palavra_sem_espaco = palavra.replace(' ', '').lower()

palavra_invertida = palavra_sem_espaco[::-1]

# Verifica se é palíndromo
if palavra_invertida == palavra_sem_espaco:
    print("Sim, é um palíndromo!")
else:
    print("Não é um palíndromo.")