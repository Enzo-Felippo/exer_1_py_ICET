red   = "\033[1;31m" 
green = "\033[0;32m"
reset = "\033[0;0m"

numeros = []

while True:
    numeros.append(int(input("\nDigite um numero: ")))

    sair = input(f"\n{green}ENTER para continuar{reset} ou {red}Digite algo para sair{reset}: ")
    if sair:
        break

numeros.sort()

print(f"O mior numero digitado é {numeros[-1]}")