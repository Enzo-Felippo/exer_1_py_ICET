red   = "\033[1;31m" 
blue  = "\033[1;34m"
green = "\033[0;32m"
reset = "\033[0;0m"
yellow = "\033[1;33m"

def eh_primo(num):
    if num <= 1:
        return False
    
    limite = num ** 0.5  
    divisor = 2

    while divisor <= limite:
        if num % divisor == 0: 
            return False
        divisor += 1 

    return True  



while True:

    numero = int(input("\n\nDigite um número: "))

    if eh_primo(numero):
        print(f"\n{blue}{numero} é um número primo.{reset}")
    else:
        print(f"\n{yellow}{numero} não é um número primo.{reset}")
    
    sair = input(f"\nAperte {green}ENTER para continuar{reset} ou {red}Digite algo para sair{reset}: ")
    if sair:
        break