populacao_a = 90_000_000
populacao_b = 200_000_000

crescimento_a = 1.03
crescimento_b = 1.015

anos = 0

while populacao_a < populacao_b:
    populacao_a = crescimento_a * populacao_a 
    populacao_b = crescimento_b * populacao_b
    anos += 1

print(f"Em {anos} anos a população A ultrapassa a população B com {int(populacao_a):,} habitantes contra {int(populacao_b):,} da população B")
