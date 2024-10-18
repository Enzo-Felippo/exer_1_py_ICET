
caractere = input("Digite um caractere: ")

if caractere.isupper():
    print(f"O caractere '{caractere}' é uma letra maiúscula.")

elif caractere.islower():
    print(f"O caractere '{caractere}' é uma letra minúscula.")

elif caractere.isdigit():
    print(f"O caractere '{caractere}' é um número.")
    
else:
    print(f"O caractere '{caractere}' é um símbolo especial ou caractere especial.")
