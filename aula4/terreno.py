#problema terreno
# declaração de variaveis
largura:float
comprimnto:float
#entrada de dados
comprimento=float(input("Digite o comprimento do terreno: "))
largura = float(input("Digite a largura do terreno: "))
valor_m2 = float(input("Digite o valor do metro quadrado: "))
#processamento de dados
area = largura * comprimento
valor_terreno = area * valor_m2
#saida de dados
print(f"A area do terreno é:, {area} m²")
print(f"O valor do terreno é: R$ {valor_terreno:.2f}")
