num = int(input("Digite um numero: "))
num1 = num
contador = 1
soma = num
while True:
    soma += num

    if num1 > num:
        break

    contador += 1
    num1 = num
    num = int(input("Digite um numero: "))

media = soma/contador

print(f"\n\nA soma dos numeros digitados é {soma}")
print(f"Você digitou {contador} numeros")
print(f"A média dos numeros digitados é {media}")
