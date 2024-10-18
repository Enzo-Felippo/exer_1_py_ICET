numeros = []
for x in range(0, 3):
    numeros.append(int(input("Digite um numero: ")))

numeros.sort()

print(f"O maior dos 3 valores distintos lidos foi  {numeros[-1]}")