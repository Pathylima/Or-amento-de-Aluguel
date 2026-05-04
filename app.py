import csv

class Imovel:
    def __init__(self, tipo, quartos, garagem, crianca):
        self.tipo = tipo
        self.quartos = quartos
        self.garagem = garagem
        self.crianca = crianca
        self.valor_base = 0
        self.valor_final = 0

    def calcular_valor(self):
        if self.tipo == "apartamento":
            self.valor_base = 700
            if self.quartos == 2:
                self.valor_base += 200
            if self.garagem:
                self.valor_base += 300
            if not self.crianca:
                self.valor_base *= 0.95  # desconto de 5%
        elif self.tipo == "casa":
            self.valor_base = 900
            if self.quartos == 2:
                self.valor_base += 250
            if self.garagem:
                self.valor_base += 300
        elif self.tipo == "estudio":
            self.valor_base = 1200
            if self.garagem:
                vagas_extras = int(input("Quantas vagas extras além das 2 inclusas? "))
                self.valor_base += 250 + (vagas_extras * 60)
        self.valor_final = self.valor_base

    def calcular_contrato(self):
        parcelas = []
        valor_contrato = 2000
        parcela_contrato = valor_contrato / 5
        for i in range(12):
            parcelas.append(round(self.valor_final + parcela_contrato, 2))
        return parcela_contrato, parcelas

    def gerar_csv(self, parcelas):
        with open("orcamento_aluguel.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Mes", "Valor Total"])
            for i, valor in enumerate(parcelas, start=1):
                writer.writerow([f"Mes {i}", f"R$ {valor:.2f}"])
        print("Arquivo CSV gerado com sucesso!")

# Programa principal
print("=== Sistema de Orçamento de Aluguel ===")
tipo = input("Digite o tipo de imóvel (apartamento/casa/estudio): ").lower()
quartos = int(input("Digite o número de quartos (1 ou 2): "))
garagem = input("Possui garagem/estacionamento? (s/n): ").lower() == "s"
crianca = input("Possui crianças? (s/n): ").lower() == "s"

imovel = Imovel(tipo=tipo, quartos=quartos, garagem=garagem, crianca=crianca)
imovel.calcular_valor()
parcela_contrato, parcelas = imovel.calcular_contrato()
imovel.gerar_csv(parcelas)

print(f"\nValor do aluguel mensal (sem contrato): R$ {imovel.valor_final:.2f}")
print(f"Parcela do contrato: R$ {parcela_contrato:.2f}")
print("Valor total mensal (aluguel + contrato):")
for i, valor in enumerate(parcelas, start=1):
    print(f"Mês {i}: R$ {valor:.2f}")