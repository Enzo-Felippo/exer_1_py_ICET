import os
from platform import system
red   = "\033[1;31m"  
forte = "\033[1;38m"
blue  = "\033[1;34m"
green = "\033[0;32m"
reset = "\033[0;0m"
yellow = "\033[1;33m"


def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b

def operar(oper: str, a: float, b: float):
    if oper == "/":
        return dividir(a, b)
    elif oper == "*":
        return multplicar(a, b)
    elif oper == "+":
        return somar(a, b)
    elif oper == "-":
        return subtrair(a, b)
    else:
        print(f"{red}O operador é invalido{reset}")

def cabecalho():
    print("="*38)
    print(f"""
          {blue}Sinais matemáticos{reset}
          {forte}Soma: +
          Subtração: -
          Multiplicação: *
          Divição: /{reset}
          {yellow}! Use (.) e não (,) ! {reset}
          """)
    print("="*38)
    print(" ")

while True:
    if system() != 'Windows':
        os.system("clear") or None
    else:
        os.system("cls") or None

    cabecalho()
    a = float(input(f"Digite o número {blue}A{reset}: "))
    oper = input("Digite o operador: ")
    b = float(input(f"Digite o número {blue}B{reset}: "))

    resutado = operar(oper, a, b)

    print(f"\n{green}Resultado: {resutado:.2f}{reset}")
    sair = input(f"\n Aperte {green}ENTER para continuar{reset} ou {red}Digite algo para sair{reset}: ")
    if sair:
        break




