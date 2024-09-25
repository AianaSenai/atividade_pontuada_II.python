import os
os.system ("cls || clear")

quantidade_numeros = 5
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = 0
menor_numero = 0
todos_pares = []
todos_impares = []
todos_numeros = []

for i in range (quantidade_numeros):
    numero = input(f"Digite o {i + 1}º numero: ")
    todos_numeros.append(numero)
    quantidade_numeros += 1

    if numero % 2 == 0:
        quantidade_pares += 1
        todos_pares.append(numero)

    else:
        quantidade_impares += 1
        todos_impares.append (numero)

maior_numero = max(todos_numeros)
menor_numero = min(todos_numeros)

soma_geral = sum(todos_numeros)
soma_pares = sum(todos_pares)
soma_impares = sum(todos_impares)

media_pares = soma_pares / quantidade_pares
media_impares = soma_impares / quantidade_pares
media_geral = soma_geral / 5

numeros_invertidos = reversed (todos_numeros)

print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")
print(f"Números na ordem inversa: {numeros_invertidos}")