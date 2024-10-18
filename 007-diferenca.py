numeros = []
diferenca = 0
pos = 0

for x in range(0, 3):
    numeros.append(int(input("Digite um numero: ")))

numeros.sort()

diferenca = numeros[2] - numeros[0]

print(f"A maior difereça é {diferenca}, entre {numeros[0], numeros[2]}")
print()
