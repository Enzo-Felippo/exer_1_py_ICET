red   = "\033[1;31m" 
green = "\033[0;32m"
reset = "\033[0;0m"

while True:

    x = int(input("\n\nDigite o primeiro numero: "))
    y = int(input("Digite o segundo numero: "))

    if x == y:
        print("São iguais")
    else:
        print(f"O maior entre {x} e {y} é {max(x, y)}")
    
    sair = input(f"\nAperte {green}ENTER para continuar{reset} ou {red}Digite algo para sair{reset}: ")
    if sair:
        break