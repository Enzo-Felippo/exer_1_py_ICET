def verificar():
    for x in str(numero):
        if x == str(alga):
            return 1
    


numero = int(input("Digite um numero: "))
alga = int(input("Digite um algarismo para ver se o anterior tinha: "))

tem = verificar()

if tem:
    print(f"O numero {alga} está no numero {numero}")
else:
    print(f"O numero {alga} não está no numero {numero}")

             